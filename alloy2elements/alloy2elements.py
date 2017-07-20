# -*- coding: utf-8 -*-


import re
import pandas as pd

extension = ".csv"
path = ""
in_file_name ="MGS_G"
in_file_name+= extension
out_file_name = "out_"+ in_file_name+ extension
critical_col=7
class alloy2elements(object):

    def __init__(self):
        pass

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

    def stringConv(self,filename):
        print("string Convertion")
        # Step 1: Load trajectories
        fr = open(filename, 'r')
        fr.readline()  # skip the header
        alloy_data = fr.readlines()
        fr.close()
        print('first line is %s '%alloy_data[0])
        print('lines = %s' %len(alloy_data))
        # Step 2: Create a dictionary to store travel time for each route per time window
        travel_times = {}  # key: route_id. Value is also a dictionary of which key is the start time for the time window and value is a list of travel times

        dataList=[]
        counter=0
        for i in range(len(alloy_data)):
            elements=[]
            data=[]
            dict_elements = {}
            each_alloy = alloy_data[i].split(',')
            alloyContent = each_alloy[0]
            Gbas = each_alloy[critical_col]
            all_inner_elements = {}


            pattern2=re.compile(r'\(')

            p1=re.compile(r'''([A-Z][a-z]?(?:[1-9]\d*|0)+(?:\.\d+)?)''')
            pattern_word=re.compile(r'([A-Z][a-z]?)')
            pattern_float=re.compile(r'((?:[1-9]\d*|0)+(?:\.\d+)?)')
            match2 = pattern2.search(alloyContent)
            if (match2):
                # print(match2.groups())
                # print(alloyContent)
                match_inner_alloy = re.findall(r'\(([A-Za-z.0-9/]*)\)(?:[1-9]\d*|0)+(?:\.\d+)?', alloyContent)
                match_inner_alloy_percent = re.findall(r'\([A-Za-z.0-9/]*\)((?:[1-9]\d*|0)+(?:\.\d+)?)', alloyContent)
                if (len(match_inner_alloy)>0):
                    # print('match3')
                    # print(match_inner_alloy_percent)
                    # print(match_inner_alloy)

                    for inner in match_inner_alloy:
                        # print(inner)
                        inner_sum=dict()
                        elements_inner=re.findall(r'([A-Z][a-z]?(?:[1-9]\d*|0)*(?:\.\d+)?)',inner)
                        # print(elements_inner)
                        if (len(elements_inner)>0):
                            for each_element_inner in elements_inner:
                                each_element_inner_percent=(self.str_to_element_and_percentage(each_element_inner))
                                all_inner_elements.update(each_element_inner_percent)
                                inner_sum.update(each_element_inner_percent)
                        # print(all_inner_elements)
                        sum_percent = (sum(inner_sum.values()))
                        # print(sum_percent)
                        for key,value in inner_sum.items():
                            # print(sum_percent)
                            # print(key,value)
                            # print(float(match_inner_alloy_percent[match_inner_alloy.index(inner)]))
                            all_inner_elements[key]=value*float(match_inner_alloy_percent[match_inner_alloy.index(inner)])/sum_percent
                        sum_percent=0
                        inner_sum.clear()
                    match_rest=re.split(r'\([A-Za-z.0-9/]*\)(?:[1-9]\d*|0)+(?:\.\d+)?', alloyContent)
                    if (match_rest):
                        match_rest.remove('')
                        # print(match_rest)
                    for strs in match_rest:
                        for m in p1.finditer(strs):
                            each_element = m.group()
                            # print(each_element)
                            matchWord = pattern_word.search(each_element)
                            match1 = pattern_float.search(each_element)
                            if (matchWord):
                                elements.append(matchWord.group())
                            if (match1):
                                data.append(float(match1.group()))
                        dict_elements = dict(zip(elements, data))
                        # print(dict_elements)
                        all_inner_elements.update(dict_elements)
                        # print(all_inner_elements)
                        all_inner_elements.update({'Gbas': float(Gbas)})
                        all_inner_elements.update({'raw':alloyContent})
                else:
                    print('no match3')
                    continue
                # print(all_inner_elements)
                dataList.append(all_inner_elements)
            ##Normal format
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

                # print(alloyContent)
                # print("Gbas=%f" % float(Gbas))
                # print(dict_elements)
                dict_elements.update({'Gbas': float(Gbas)})
                dict_elements.update({'raw': alloyContent})
                dataList.append(dict_elements)
            counter+=1
            # print("-----------------------------------------%d"%counter)

        return dataList

    def writeCSV(self,df=pd.DataFrame, output_filename=str):
        print("write csv file")
        df.to_csv(output_filename, encoding='utf-8')
    def toAlloy(self):
        print("to alloy")

    def toElements(self,dataList):
        print("to elements")
        df=pd.DataFrame(dataList)
        #print(df)
        return df


def main():
    print("This script is used to convert alloy to elements.")

    work1 = alloy2elements()

    dataList = work1.stringConv(path+in_file_name)
    # print(len(dataList))
    dataFrame = work1.toElements(dataList)
    dataFrame.fillna(0.0, inplace=True)
    # print(dataFrame)
    work1.writeCSV(dataFrame,out_file_name)

if __name__ == '__main__':
    main()
