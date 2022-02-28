import customer_class as cust
import car_class as car
import service_quote_class as sq

def main():
    my_cust = cust.Customer('Lanie Williams','1411 Paseo de Vaca San Angelo, TX 76901','325-656-4124')
    my_car = car.Car('Toyota','4-Runner','2016')
    my_sq = sq.ServiceQuote(500, 200)

    print("Name: ",my_cust.get_name())
    print("Address: ",my_cust.get_address())
    print("Phone: ",my_cust.get_phone())
    print('-------------------------')
    print("Manufacturer: ",my_car.get_make())
    print("Model: ",my_car.get_model())
    print("Year: $",my_car.get_year())
    print('-------------------------')

    print("Labor Charge:", my_sq.get_labor_charges())
    print("Parts Charge:", my_sq.get_parts_charges())
    print("Sales Tax:", my_sq.get_sales_tax())
    print("Total Charge:", my_sq.get_total_charges())


   


main()