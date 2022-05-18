from database.normalitycheck import normalitycheck_fit_shapiro_wilk

database_name="main_database_aux.db"

if __name__ == '__main__':
    normalitycheck_fit_shapiro_wilk.normalitycheck_fit_shapiro_wilk(database_name)
