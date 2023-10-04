import pandas as pd
import os
class PhoneBookManager:
    def __init__(self, file_name='data.xlsx'):
        self.file_name = file_name
        # Create an initial (empty) data frame or read from a file if one exists
        # Check the existence of the file
        if os.path.isfile(self.file_name):
            self.df = pd.read_excel(self.file_name)
        else:
            self.df = pd.DataFrame()

    # ------------------------------------------------------

    def add_contact(self, message):
        # Convert input data to a new dataframe
        df = pd.DataFrame(message)

        #Adding a new dataframe to the main dataframe
        self.df = pd.concat([self.df, df], ignore_index=True)

        # Save the dataframe to an Excel file
        self.df.to_excel(self.file_name, index=False)

        print('Data saved successfully.')
        print("Contact added successfully.")

    # --------------------------------------------------------
    def show_contacts(self):
        if not self.df.empty:
            print("\nContacts:")
            for index, row in self.df.iterrows():
                print(f"country_code: {row['country_code']}, Phone Number: {row['phone_number']}, Name: {row['Name']}, Email: {row['Email']}")
        else:
            print("No contacts to display.")

    # ----------------------------------------------------------------
    def save_and_exit(self, file_name):
        self.df.to_excel(file_name, index=False, engine='openpyxl')
        print(f"Contacts saved to '{file_name}'. Exiting the program.")

    # ----------------------------------------------------------------

    def search_by_name(self, name):
        # Search by name
        result = self.df[self.df['Name'] == name]
        return result
    # ----------------------------------------------------------

    def delete_by_name(self, name):
        # Check if the name exists in the data
        if name in self.df['Name'].values:
            #Delete records matching the name
            self.df = self.df[self.df['Name'] != name]

            self.df.to_excel(self.file_name, index=False)

            print(f'Records with the name "{name}" deleted successfully.')
        else:
            print(f'No records found with the name "{name}".')
    # ----------------------------------------------------------------------------