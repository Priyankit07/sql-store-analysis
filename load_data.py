{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "119cb714",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pymysql in c:\\users\\admin\\miniconda3\\lib\\site-packages (1.1.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n",
      "[✓] Imported 'C:\\Users\\ADMIN\\Downloads\\archive (3)\\brands.csv' into table 'brands'\n",
      "[✓] Imported 'C:\\Users\\ADMIN\\Downloads\\archive (3)\\categories.csv' into table 'categories'\n",
      "[✓] Imported 'C:\\Users\\ADMIN\\Downloads\\archive (3)\\customers.csv' into table 'customers'\n",
      "[✓] Imported 'C:\\Users\\ADMIN\\Downloads\\archive (3)\\order_items.csv' into table 'order_items'\n",
      "[✓] Imported 'C:\\Users\\ADMIN\\Downloads\\archive (3)\\orders.csv' into table 'orders'\n",
      "[✓] Imported 'C:\\Users\\ADMIN\\Downloads\\archive (3)\\products.csv' into table 'products'\n",
      "[✓] Imported 'C:\\Users\\ADMIN\\Downloads\\archive (3)\\staffs.csv' into table 'staffs'\n",
      "[✓] Imported 'C:\\Users\\ADMIN\\Downloads\\archive (3)\\stocks.csv' into table 'stocks'\n",
      "[✓] Imported 'C:\\Users\\ADMIN\\Downloads\\archive (3)\\stores.csv' into table 'stores'\n"
     ]
    }
   ],
   "source": [
    "%pip install pymysql\n",
    "\n",
    "import pandas as pd\n",
    "from sqlalchemy import create_engine\n",
    "import os\n",
    "from dotenv import load_dotenv\n",
    "\n",
    "# Load environment variables\n",
    "load_dotenv()\n",
    "\n",
    "# Database credentials from .env file\n",
    "user = os.getenv(\"MYSQL_USER\", \"root\")\n",
    "password = os.getenv(\"MYSQL_PASSWORD\", \"Password\")\n",
    "db = os.getenv(\"MYSQL_DB\", \"karma2\")\n",
    "\n",
    "# Connect to MySQL\n",
    "engine = create_engine(f\"mysql+pymysql://{user}:{password}@localhost/{db}\")\n",
    "\n",
    "# CSV file to table name mapping\n",
    "csv_table_map = {\n",
    "    r\"C:\\Users\\ADMIN\\Downloads\\archive (3)\\brands.csv\": \"brands\",\n",
    "    r\"C:\\Users\\ADMIN\\Downloads\\archive (3)\\categories.csv\": \"categories\",\n",
    "    r\"C:\\Users\\ADMIN\\Downloads\\archive (3)\\customers.csv\": \"customers\",\n",
    "    r\"C:\\Users\\ADMIN\\Downloads\\archive (3)\\order_items.csv\": \"order_items\",\n",
    "    r\"C:\\Users\\ADMIN\\Downloads\\archive (3)\\orders.csv\": \"orders\",\n",
    "    r\"C:\\Users\\ADMIN\\Downloads\\archive (3)\\products.csv\": \"products\",\n",
    "    r\"C:\\Users\\ADMIN\\Downloads\\archive (3)\\staffs.csv\": \"staffs\",\n",
    "    r\"C:\\Users\\ADMIN\\Downloads\\archive (3)\\stocks.csv\": \"stocks\",\n",
    "    r\"C:\\Users\\ADMIN\\Downloads\\archive (3)\\stores.csv\": \"stores\",\n",
    "}\n",
    "\n",
    "# Import each CSV\n",
    "for file, table in csv_table_map.items():\n",
    "    try:\n",
    "        df = pd.read_csv(file)\n",
    "        df.to_sql(table, con=engine, index=False, if_exists='replace')\n",
    "        print(f\"[✓] Imported '{file}' into table '{table}'\")\n",
    "    except Exception as e:\n",
    "        print(f\"[✗] Failed to import '{file}': {e}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8e33e87",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
