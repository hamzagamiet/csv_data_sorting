import os
import csv
from pathlib import Path
import pandas as pd
import openpyxl


def main():
    print("starting process...")
    BASE_DIR = Path(__file__).resolve().parent
    invoices_folder = os.path.join(BASE_DIR, "invoices")
    adm_dis_folder = os.path.join(BASE_DIR, "admission_discharge")
    occupancy_folder = os.path.join(BASE_DIR, "occupancy")
    get_invoice(invoices_folder, BASE_DIR)
    get_adm_dis(adm_dis_folder, BASE_DIR)
    get_occupancy(occupancy_folder, BASE_DIR)


def get_invoice_data(data):
    context = {
        "invoice_no": "",
        "dates": "",
        "account_no": "",
        "resident_no": "",
        "source": "",
        "details": "",
        "transaction_amount": "",
    }

    for key in data:
        if "invoice_no" in key:
            context["invoice_no"] = data[key]
        if "date" in key:
            context["dates"] = data[key]
        if "account_no" in key:
            context["account_no"] = data[key]
        if "resident_no" in key:
            context["resident_no"] = data[key]
        if "source" in key:
            context["source"] = data[key]
        if "details" in key:
            context["details"] = data[key]
        if "transaction_amount" in key:
            context["transaction_amount"] = data[key]

    return context


def invoices_csv(BASE_DIR, invoice_data, file_no):
    master_invoice_file = os.path.join(BASE_DIR, "master_invoice.csv")
    print(invoice_data["dates"])
    # create new master_invoice when adding data from the first file
    if file_no == 0:
        with open(
            master_invoice_file, "w+", encoding="UTF8", newline=""
        ) as invoice_master:
            writer = csv.writer(invoice_master)
            writer.writerow(key for key in invoice_data)
            for x in range(len(invoice_data["invoice_no"])):
                writer.writerow(
                    [
                        invoice_data["invoice_no"][x],
                        invoice_data["dates"][x],
                        invoice_data["account_no"][x],
                        invoice_data["resident_no"][x],
                        invoice_data["source"][x],
                        invoice_data["details"][x],
                        invoice_data["transaction_amount"][x],
                    ]
                )
    # append data to master_invoice for every file other than the first file
    else:
        with open(
            master_invoice_file, "a+", encoding="UTF8", newline=""
        ) as invoice_master:
            writer = csv.writer(invoice_master)
            for x in range(0, len(invoice_data["invoice_no"])):
                writer.writerow(
                    [
                        invoice_data["invoice_no"][x],
                        invoice_data["dates"][x],
                        invoice_data["account_no"][x],
                        invoice_data["resident_no"][x],
                        invoice_data["source"][x],
                        invoice_data["details"][x],
                        invoice_data["transaction_amount"][x],
                    ]
                )
    invoice_master.close()
    return


def get_invoice(invoices_folder, BASE_DIR):
    file_no = 0
    for file in os.listdir(invoices_folder):
        print(f"FILE {file_no+1}: {file}")
        # try reading file as CSV
        file_to_open = os.path.join(invoices_folder, file)
        try:
            data = pd.read_csv(file_to_open)
        except:
            print("file is not in the correct format")
        # pull column data from CSV file
        invoice_data = get_invoice_data(data)
        invoices_csv(BASE_DIR, invoice_data, file_no)
        file_no += 1



def get_adm_dis_data(data):
    context = {
        "res_code": "",
        "dates": "",
        "res_name": "",
        "res_current": "",
        "admission": "",
        "discharge": "",
        "description": "",
    }

    for key in data:
        if "res_code" in key:
            context["res_code"] = data[key]
        if "date" in key:
            context["dates"] = data[key]
        if "res_name" in key:
            context["res_name"] = data[key]
        if "res_current" in key:
            context["res_current"] = data[key]
        if "admission" in key:
            context["admission"] = data[key]
        if "discharge" in key:
            context["discharge"] = data[key]
        if "description" in key:
            context["description"] = data[key]

    return context



def adm_dis_csv(BASE_DIR, adm_dis_data, file_no):
    master_adm_dis_file = os.path.join(BASE_DIR, "master_adm_dis.csv")
    print(adm_dis_data["res_code"])
    # create new master_adm_dis when adding data from the first file
    if file_no == 0:
        with open(
            master_adm_dis_file, "w+", encoding="UTF8", newline=""
        ) as adm_dis_master:
            writer = csv.writer(adm_dis_master)
            writer.writerow(key for key in adm_dis_data)
            for x in range(len(adm_dis_data["dates"])):
                writer.writerow(
                    [
                        adm_dis_data["res_code"][x],
                        adm_dis_data["dates"][x],
                        adm_dis_data["res_name"][x],
                        adm_dis_data["res_current"][x],
                        adm_dis_data["admission"][x],
                        adm_dis_data["discharge"][x],
                        adm_dis_data["description"][x],
                    ]
                )
    # append data to master_adm_dis for every file other than the first file
    else:
        with open(
            master_adm_dis_file, "a+", encoding="UTF8", newline=""
        ) as adm_dis_master:
            writer = csv.writer(adm_dis_master)
            for x in range(0, len(adm_dis_data["adm_dis_no"])):
                writer.writerow(
                    [
                        adm_dis_data["res_code"][x],
                        adm_dis_data["dates"][x],
                        adm_dis_data["res_name"][x],
                        adm_dis_data["res_current"][x],
                        adm_dis_data["admission"][x],
                        adm_dis_data["discharge"][x],
                        adm_dis_data["description"][x],
                    ]
                )
    adm_dis_master.close()
    return


    
def get_adm_dis(adm_dis_folder, BASE_DIR):
    file_no = 0
    for file in os.listdir(adm_dis_folder):
        print(f"FILE {file_no+1}: {file}")
        # try reading file as CSV
        file_to_open = os.path.join(adm_dis_folder, file)
        try:
            data = pd.read_csv(file_to_open)
        except:
            print("file is not in the correct format")
        # pull column data from CSV file
        adm_dis_data = get_adm_dis_data(data)
        adm_dis_csv(BASE_DIR, adm_dis_data, file_no)
        file_no += 1



def get_occupancy_data(data):
    context = {
        "dates": "",
        "occ_level": "",
    }

    for key in data:
        if "date" in key:
            context["dates"] = data[key]
        elif "occ" in key and "level" in key:
            context["occ_level"] = data[key]

    return context


def occupancy_csv(BASE_DIR, occupancy_data, file_no):
    master_occupancy_file = os.path.join(BASE_DIR, "master_occupancy.csv")
    print(occupancy_data["dates"])
    # create new master_occupancy when adding data from the first file
    if file_no == 0:
        with open(
            master_occupancy_file, "w+", encoding="UTF8", newline=""
        ) as occupancy_master:
            writer = csv.writer(occupancy_master)
            writer.writerow(key for key in occupancy_data)
            for x in range(len(occupancy_data["dates"])):
                writer.writerow(
                    [
                        occupancy_data["dates"][x],
                        occupancy_data["occ_level"][x],
                    ]
                )
    # append data to master_occupancy for every file other than the first file
    else:
        with open(
            master_occupancy_file, "a+", encoding="UTF8", newline=""
        ) as occupancy_master:
            writer = csv.writer(occupancy_master)
            for x in range(0, len(occupancy_data["dates"])):
                writer.writerow(
                    [
                        occupancy_data["dates"][x],
                        occupancy_data["occ_level"][x],
                    ]
                )
    occupancy_master.close()
    return


def get_occupancy(occupancy_folder, BASE_DIR):
    file_no = 0
    for file in os.listdir(occupancy_folder):
        print(f"FILE {file_no+1}: {file}")
        # try reading file as CSV
        file_to_open = os.path.join(occupancy_folder, file)
        try:
            data = pd.read_csv(file_to_open)
        except:
            print("file is not in the correct format")
        # pull column data from CSV file
        occupancy_data = get_occupancy_data(data)
        occupancy_csv(BASE_DIR, occupancy_data, file_no)
        file_no += 1


main()
