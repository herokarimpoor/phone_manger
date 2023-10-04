from phonebook import PhoneBookManager

phonebook_manager = PhoneBookManager()


class GetParams:

    @staticmethod
    def make_create_phone_message(country_code, number, name, email):
        message = {
            'country_code': [country_code],
            'phone_number': [number],
            'Name': [name],
            'Email': [email]
        }

        phonebook_manager.add_contact(message=message)
        return message


    # -------------------------------------------------------------------------

    @staticmethod
    def invoke_create_new_number():
        country_code = input('Please enter country_code: ')
        phone_Number = input('Please enter phone_number: ')
        Name = input('Please enter Name: ')
        Email = input('Please enter a Email: ')

        message = GetParams.make_create_phone_message(country_code=country_code, phone_number=Number, name=Name, email=Email)

        print('#### message:', message)
        return message

    # ---------------------------------------------------------------------

