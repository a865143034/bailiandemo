#coding:utf-8
import xlrd

def getTitle():
    fname="/Users/wangkun/Desktop/comdata/titlelist.xlsx"
    bk = xlrd.open_workbook(fname)
    #shxrange = range(bk.nsheets)
    try:#try和except是最常用的异常处理
        sh = bk.sheet_by_name("工作表1")
    except:
        print("no sheet in %s named Sheet1" % fname)
    nrows = sh.nrows
    #ncols = sh.ncols
    #print(nrows,ncols)
    #print(nrows,ncols)
    # 获取第一行第一列数据
    #cell_value = sh.cell_value(1, 1)
    row_list = []
    for i in range(0,nrows):
        row_data = sh.row_values(i)
        row_list.append(row_data[0])
    return row_list


def getCompany():
    fname="/Users/wangkun/Desktop/comdata/comlist1.xlsx"
    bk = xlrd.open_workbook(fname)
    try:
        sh = bk.sheet_by_name("工作表1")
    except:
        print("no sheet in %s named Sheet1" % fname)
    nrows = sh.nrows
    ncols=sh.ncols
    print(nrows,ncols)
    row_list = []
    for i in range(0,nrows):
        tmplist=[]
        for j in range(0,ncols):
            row_data = sh.row_values(i)
            tmplist.append(row_data)
    row_list.append(tmplist)
    return row_list


getCompany()