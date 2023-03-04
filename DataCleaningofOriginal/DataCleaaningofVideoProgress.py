import win32com.client as win32
import openpyxl

# 将xls文件转为xlsx文件
# fname = "K:\\bishe\\SchoolPrecaution\\data\\视频\\数据结构与算法视频学习数据统计.xls"
# excel = win32.gencache.EnsureDispatch('Excel.Application')
# wb = excel.Workbooks.Open(fname)
#
# wb.SaveAs(fname + "x", FileFormat=51)  # FileFormat = 51 is for .xlsx extension
# wb.Close()  # FileFormat = 56 is for .xls extension
# excel.Application.Quit()

# 确定文件数据所在根目录
src_path = "../data"
# 确定文件保存的新目录
save_src_path = "../cleanedData"
def openFile(src_path,ExperimentalCheck_path,ExperimentalCheck_name,save_src_path,save_path):
    # 获取查重文件的完整路径
    wholePath = src_path + ExperimentalCheck_path + ExperimentalCheck_name;
    print("完整路径为："+wholePath)
    # 使用openpyxl加载文件
    file = openpyxl.load_workbook(wholePath)
    print("已加载文件")
    # 根据sheet名称获取要操作的指定sheet页
    sheet = file['原始数据']
    print("指定sheet页")
    # 读取表内所有数据
    data_of_row = list(sheet.rows)
    # for row in sheet.rows:
    #     for cell in row:
    #         print(cell.value)
    file_act = file.active
    # 获取该文件中的最大行数
    file_rows_max_nums = file_act.max_row
    # 起始行，由于存在3行表头，故为3
    row_n = 2
    # 目标列，为第一列，主要为了取出多余数据
    col_n = 5
    i = 1
    while i < file_rows_max_nums:
        if file_act.cell(row=row_n,column=col_n).value != '21级软件1-2班':
            file_act.delete_rows(row_n)
            print("已删除第"+str(row_n)+"行")
        else:
            row_n += 1
        i += 1
    save_name = save_src_path + save_path + ExperimentalCheck_name
    print(save_name)
    file.save(save_name)
    print("已成功保存"+ExperimentalCheck_name)


# 进行实验查重文件的清洗过程
# 确定实验查重文件所在的目录
ExperimentalCheck_path = "/视频"
# 要保存的路径
save_path = "/VideoProgress"

# 确定文件名称，并访问打开文件从而进行数据清洗
for i in range(1,2):
    # 要查重文件的名称
    ExperimentalCheck_name = "/数据结构与算法视频学习数据统计.xlsx"
    # 打印要查重文件的名称
    print(ExperimentalCheck_name)
    # 从系统中根据文件目录打开文件
    openFile(src_path,ExperimentalCheck_path,ExperimentalCheck_name,save_src_path,save_path)
