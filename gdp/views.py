from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from .models import Gdp
from .serializers import GdpSerializer
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt


class GdpApi(APIView):

    def get(self, request):
        try:
            payload = []
            data = pd.read_excel('/home/sagar/Documents/india_gdp.xlsx')
            for row in data.itertuples():
                year = str(row[1])[0:4]
                print(year)
                payload.append(Gdp(year=int(year), gdp_usd_billion=row[2]))
            Gdp.objects.bulk_create(payload)
            return Response(status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GdpChartApi(APIView):

    def get(self, request):
        try:
            year_x = []
            inr_y = []
            usd_y = []
            rate = requests.get(
                'https://api.currencyfreaks.com/v2.0/rates/latest?apikey=accb15ec4147450f9dce007d3e8b9d15').json()[
                'rates']['INR']
            #rate = 82.02
            gdp_data = Gdp.objects.all()
            serializer = GdpSerializer(gdp_data, many=True)
            for i in serializer.data:
                # print(dict(i)['gdp_usd_billion'], dict(i)['year'])
                year_x.append(dict(i)['year'])
                usd_y.append(dict(i)['gdp_usd_billion'])
                inr_y.append(dict(i)['gdp_usd_billion'] * float(rate))
            print(len(inr_y))
            print(len(usd_y))

            x = np.array(year_x)
            y = np.array(usd_y)

            # create initial plot
            fig, ax = plt.subplots()
            line, = ax.plot(x, y)
            ax.set_xlabel('Year')
            ax.set_ylabel("'India\'s GDP in USD billions")

            # define button click action
            def on_button_click(event):

                new_y = np.array(inr_y)
                line.set_ydata(new_y)
                ax.set_ylim(new_y.min(), new_y.max())
                ax.set_xlabel('Year')
                ax.set_ylabel("'India\'s GDP in INR")

                line.set_label('New Data')
                # update legend
                ax.legend()

                # update plot
                fig.canvas.draw()

            # create button
            button_ax = plt.axes([0.7, 0.9, 0.1, 0.1])
            button = plt.Button(button_ax, 'Convert')

            # button on-click action
            button.on_clicked(on_button_click)

            # show plot
            plt.show()

            return Response(status=status.HTTP_200_OK)
        except Exception as err:
            print("error", err)
            return Response(status=status.HTTP_400_BAD_REQUEST)
