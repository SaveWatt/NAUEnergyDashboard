# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import pandas as pd
import csv
import numpy as np
import pymysql.cursors
#from django.views.generic import TemplateView

def home(request):
    return render(request,'index.html')

def export(request):
#     Create the HttpResponse object with the appropriate CSV header.
#    data = pd.read_csv('C:\Users\Master\Documents\Capstone\testCSV.csv')

    return render(request, 'export.html')

def export_data(request):
    conn = pymysql.connect(host='localhost',
    user='root',
    password='',
    db='test_my_database',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

    sql = 'SELECT Sample_Value, Time_Of_Sample FROM tblTrendlog_0000100_0000000001'
    data = pd.read_sql('SELECT Sample_Value, Time_Of_Sample FROM tblTrendlog_0000100_0000000001', conn)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="DEV100INST00001.csv"'
    writer = csv.writer(response)
    writer.writerow(data)

    #data.to_csv('DEV100INST00001.csv')
    return response

def export_file(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['Sample_data', 'Time_Of_Sample'])
    writer.writerow(['',''])
    writer.writerow(['',''])
    writer.writerow(['',''])
    writer.writerow(['',''])
    writer.writerow(['',''])
    writer.writerow(['',''])
    writer.writerow(['',''])
    writer.writerow(['',''])
    writer.writerow(['',''])
    writer.writerow(['',''])

    return response

def comparson(request):
    return render(request, 'comparison.html')


def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


def Clean(data):


    #filling in data with N/A
    data.fillna("N/A",inplace=True)

    #removing Unames colomn
    data.drop('Unnamed: 0', axis=1, inplace=True)


    #removing duplicats in Time_in_sample
    Remove(data['Time_Of_Sample'])

    return data


def test(request):
    conn = pymysql.connect(host='localhost',
    user='root',
    password='',
    db='test_my_database',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

    sql = 'SELECT Sample_Value, Time_Of_Sample FROM tblTrendlog_0000100_0000000001'
    data = pd.read_sql('SELECT Sample_Value, Time_Of_Sample FROM tblTrendlog_0000100_0000000001', conn)

    print(pd.read_sql('SELECT Sample_Value, Time_Of_Sample FROM tblTrendlog_0000100_0000000001', conn))
    return render(request,'comparison.html')

def comparson_d(request):
    """
        <div id="div-container">
        <canvas id="line-chart"></canvas>
        </div>

    <script>
    new Chart(document.getElementById("line-chart"), {
      type: 'line',
      data: {
        labels: [
          <?php
              $conn = mysqli_connect("10.18.167.68", "root", "", "test_my_database");

              $query = 'SELECT Time_Of_Sample FROM tblTrendlog_0000100_0000000001 WHERE Sequence BETWEEN 1 AND 500';
              $result = mysqli_query($conn, $query);

              while( $row = mysqli_fetch_array($result) ) {
                echo '"'.$row['Time_Of_Sample'].'",';
              }
              mysqli_close($conn);
            ?>
          ],
        fillOpacity: .3,
        datasets: [{
            data: [
              <?php
                $conn = mysqli_connect("10.18.167.68", "", "", "test_my_database");

                $query = 'SELECT Sample_Value FROM tblTrendlog_0000100_0000000001 WHERE Sequence BETWEEN 1 AND 500';
                $result = mysqli_query($conn, $query);
                while( $row = mysqli_fetch_array($result) ) {
                	echo $row['Sample_Value'] . ',';
                }
                mysqli_close($conn);
              ?>],
            label: "Week 1",
            borderColor: "#1f61a8",
            fill: origin,
            backgroundColor: "rgba(31,97,168,.3)",
          }
        ]
      },
      options: {
        responsive: false,
        title: {
          display: true,
          text: "SAS Building Electricity usage",
        },
        scales: {
        xAxes: [{
          scaleLabel: {
            display: true,
            labelString: 'Time'
          }
        }],
        yAxes: [{
          scaleLabel: {
            display: true,
            labelString: 'Electricity (kWh)'
          }
        }]
      }
      }
    });
    </script>




    """


#class home(TemplateView):
#    template_name = "index.html"
#from django.http import HttpResponse

#data = pd.read_csv(r'testCSV.csv')

#def home(request):
#    return HttpResponse('data')

#from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse

#def home(request):
    # Create the HttpResponse object with the appropriate CSV header.
#    response = HttpResponse(content_type='text/csv')
#    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
#
#    writer = csv.writer(response)
#    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
#    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

#    return response

#from django.shortcuts import render
#from django.conf import settings
#from django.core.files.storage import FileSystemStorage

#def home(request):
#    if request.method == 'POST' and request.FILES['myfile']:
#        myfile = request.FILES['myfile']
#        fs = FileSystemStorage()
#        filename = fs.save(myfile.name, myfile)
#        uploaded_file_url = fs.url(filename)
#        return render(request, 'core/simple_upload.html', {
#            'uploaded_file_url': uploaded_file_url
#        })
#    return render(request, 'core/simple_upload.html')
