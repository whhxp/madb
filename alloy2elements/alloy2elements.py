# -*- coding: utf-8 -*-



import math
from datetime import datetime,timedelta
import re


extension = ".csv"
path = ""
in_file_name ="MGS_G"
in_file_name+= extension
out_file_name = "out" + extension

class alloy2elements(object):

    def __init__(self):
        pass

    def readcsv(self):
        print("read csv")

    def str_to_element_and_percentage(self, str_element):
        dict_element = dict()
        pattern_word = re.compile(r'([A-Z][a-z]?)')
        pattern_float = re.compile(r'((?:[1-9]\d*|0)+(?:\.\d+)?)')
        matchWord = pattern_word.search(str_element)
        match1 = pattern_float.search(str_element)
        if (matchWord):
            element_name=(matchWord.group())
        if (match1):
            element_data=float(match1.group())
        else:
            element_data=1
        dict_element[element_name]=element_data
        return dict_element

    def stringConv(self):
        print("string Convertion")
        # Step 1: Load trajectories
        fr = open(path + in_file_name, 'r')
        fr.readline()  # skip the header
        alloy_data = fr.readlines()
        fr.close()
        print(alloy_data[0])

        # Step 2: Create a dictionary to store travel time for each route per time window
        travel_times = {}  # key: route_id. Value is also a dictionary of which key is the start time for the time window and value is a list of travel times

        data1={}
        for i in range(len(alloy_data)):
            elements=[]
            data=[]
            dict_elements = {}
            each_alloy = alloy_data[i].replace('"', '').split(',')
            alloyContent = each_alloy[0]
            Gbas = each_alloy[7]



            pattern2=re.compile(r'\(')

            p1=re.compile(r'''([A-Z][a-z]?(?:[1-9]\d*|0)+(?:\.\d+)?)''')
            pattern_word=re.compile(r'([A-Z][a-z]?)')
            pattern_float=re.compile(r'((?:[1-9]\d*|0)+(?:\.\d+)?)')
            match2 = pattern2.search(alloyContent)
            if (match2):
                # print(match2.groups())
                print(alloyContent)
                match_inner_alloy = re.findall(r'(\([A-Za-z.0-9/]*\)(?:[1-9]\d*|0)+(?:\.\d+)?)', alloyContent)
                if (match_inner_alloy):
                    print('match3')
                    # match4=re.match(r'',match4.group())
                    # if (match4):
                    #     print(match4.groups())
                    print(match_inner_alloy)
                    for inner in match_inner_alloy:
                        elements_inner=re.findall(r'([A-Z][a-z]?(?:[1-9]\d*|0)*(?:\.\d+)?)',inner)
                        print(elements_inner)
                        if (elements_inner):
                            for each_element_inner in elements_inner:
                                print(self.str_to_element_and_percentage(each_element_inner))
                else:
                    print('no match3')
            else:
                for m in p1.finditer(alloyContent):
                    each_element=m.group()
                    # print(each_element)
                    matchWord=pattern_word.search(each_element)
                    match1=pattern_float.search(each_element)
                    if (matchWord):
                        elements.append(matchWord.group())
                    if(match1):
                        data.append(float(match1.group()))
                dict_elements = dict(zip(elements, data))

                print(alloyContent)
                print("Gbas=%f" % float(Gbas))
                print(dict_elements)
            print("-----------------------------------------")
            # route_id = intersection_id + '-' + tollgate_id
            # if route_id not in travel_times.keys():
            #     travel_times[route_id] = {}
            #
            # trace_start_time = each_traj[3]
            # trace_start_time = datetime.strptime(trace_start_time, "%Y-%m-%d %H:%M:%S")
            # time_window_minute = math.floor(trace_start_time.minute / 20) * 20
            # start_time_window = datetime(trace_start_time.year, trace_start_time.month, trace_start_time.day,
            #                              trace_start_time.hour, time_window_minute, 0)
            # tt = float(each_traj[-1])  # travel time
            #
            # if start_time_window not in travel_times[route_id].keys():
            #     travel_times[route_id][start_time_window] = [tt]
            # else:
            #     travel_times[route_id][start_time_window].append(tt)

        # Step 3: Calculate average travel time for each route per time window
        # fw = open(out_file_name, 'w')
        # fw.writelines(','.join(['"intersection_id"', '"tollgate_id"', '"time_window"', '"avg_travel_time"']) + '\n')
        # for route in travel_times.keys():
        #     route_time_windows = list(travel_times[route].keys())
        #     route_time_windows.sort()
        #     for time_window_start in route_time_windows:
        #         time_window_end = time_window_start + timedelta(minutes=20)
        #         tt_set = travel_times[route][time_window_start]
        #         avg_tt = round(sum(tt_set) / float(len(tt_set)), 2)
        #         out_line = ','.join(['"' + route.split('-')[0] + '"', '"' + route.split('-')[1] + '"',
        #                              '"[' + str(time_window_start) + ',' + str(time_window_end) + ')"',
        #                              '"' + str(avg_tt) + '"']) + '\n'
        #         fw.writelines(out_line)
        # fw.close()

    def writeCSV(self):
        print("write csv file")

    def toAlloy(self):
        print("to alloy")

    def toElements(self):
        print("to elements")

def main():
    print("This script is used to convert alloy to elements.")

    work1 = alloy2elements()

    work1.readcsv()
    work1.stringConv()
    work1.writeCSV()


if __name__ == '__main__':
    main()
