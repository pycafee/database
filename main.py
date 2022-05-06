
"""Perform all DDL and DML commands to create fresh new database and perform tests to check if everything is correct.

The order of creation and insertion of information into the database is important, as well as the order of testing is vital.

The execution sequence should be as follows:

1. creating_db.creating_database()
    --> Creates the "main_database.db" database
2. tests/test_creating_database/test_creating_db.py
    --> Tests if the table "main_database.db" was created correctly
3. tests/test_creating_database/test_creating_db.py
    --> Tests if the constraints of the "main_database.db" works as expected
4. basic_inserts.basic_inserts()
    --> Performs all the basic inserts in the "main_database.db"



Author: Anderson Marcos Dias Canteli <andersonmdcanteli@gmail.com>

Created: 4th April, 2022.

"""


import os
import winsound
from database import creating_db, basic_inserts, default_inserts
from database import insert_02, insert_03, insert_04 # Normality tests

from database.checkers import _check_is_bool, _check_is_data_frame, _check_is_dict, _check_is_float_or_int
from database.checkers import _check_is_float, _check_is_integer, _check_is_list, _check_is_numpy_1_D
from database.checkers import _check_is_str, _check_data_in_range, _check_is_positive
from database.distributions import get_shapiro_wilk_tabulated_value, shapiro_wilk, ShapiroWilkNormalityTest, draw_shapiro_wilk_tabulated_values, shapiro_wilk_to_csv, shapiro_wilk_to_xlsx
from database.helpers import _change_locale, _export_to_csv, _check_forbidden_character, _export_to_excel, _check_conflicting_filename, LanguageManagement, AlphaManagement, NDigitsManagement
from database.helpers import _check_blank_space, _sep_checker, _check_figure_extension, _flat_list_of_lists, _check_plot_design, _check_which_density_gaussian_kernal_plot
from database.helpers import _check_file_name_is_str
from database.functions import multimode
from database.plots import draw_dot_plot, draw_density_function
# from database import insert_06 # management



database_name="main_database.db"



if __name__ == '__main__':
    try:
        # 1.
        creating_db.creating_database(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        # 2.
        os.system("python -m unittest -v tests/test_creating_database/test_creating_db.py")
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        # 3.
        os.system("python -m unittest -v tests/test_creating_database/test_database_constraints.py")
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)

        basic_inserts.basic_inserts(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("basic_inserts was added")

        default_inserts.insert_default_inserts(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("insert_default_inserts was added")

        insert_02.insert_kolmogorov_smirnov(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("insert_kolmogorov_smirnov was added")

        insert_03.insert_anderson_darling(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("insert_anderson_darling was added")

        insert_04.insert_lilliefors(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("insert_lilliefors was added")


        _check_is_bool._check_is_bool(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_is_bool was added")

        _check_is_data_frame._check_is_data_frame(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_is_data_frame was added")

        _check_is_dict._check_is_dict(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_is_dict was added")

        _check_is_float_or_int._check_is_float_or_int(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_is_float_or_int was added")

        _check_is_float._check_is_float(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_is_float was added")

        _check_is_integer._check_is_integer(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_is_integer was added")

        _check_is_list._check_is_list(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_is_list was added")

        _check_is_numpy_1_D._check_is_numpy_1_D(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_is_numpy_1_D was added")

        _check_is_str._check_is_str(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_is_str was added")

        _change_locale._change_locale(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_change_locale was added")

        get_shapiro_wilk_tabulated_value.get_shapiro_wilk_tabulated_value(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("get_shapiro_wilk_tabulated_value was added")

        shapiro_wilk.shapiro_wilk(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("shapiro_wilk was added")

        _check_data_in_range._check_data_in_range(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_data_in_range was added")

        ShapiroWilkNormalityTest.ShapiroWilkNormalityTest(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("ShapiroWilkNormalityTest was added")

        _check_is_positive._check_is_positive(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_is_positive was added")

        _export_to_csv._export_to_csv(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_export_to_csv was added")

        _check_forbidden_character._check_forbidden_character(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_forbidden_character was added")

        _export_to_excel._export_to_excel(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_export_to_excel was added")

        draw_shapiro_wilk_tabulated_values.draw_shapiro_wilk_tabulated_values(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("draw_shapiro_wilk_tabulated_values was added")

        shapiro_wilk_to_csv.shapiro_wilk_to_csv(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("shapiro_wilk_to_csv was added")

        shapiro_wilk_to_xlsx.shapiro_wilk_to_xlsx(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("shapiro_wilk_to_xlsx was added")

        multimode.multimode(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("multimode was added")

        _check_conflicting_filename._check_conflicting_filename(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_conflicting_filename was added")

        draw_dot_plot.draw_dot_plot(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("draw_dot_plot was added")

        draw_density_function.draw_density_function(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("draw_density_function was added")

        LanguageManagement.LanguageManagement(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("LanguageManagement was added")

        AlphaManagement.AlphaManagement(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("AlphaManagement was added")

        NDigitsManagement.NDigitsManagement(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("NDigitsManagement was added")

        _check_blank_space._check_blank_space(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_blank_space was added")

        _sep_checker._sep_checker(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_sep_checker was added")

        _check_figure_extension._check_figure_extension(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_figure_extension was added")

        _flat_list_of_lists._flat_list_of_lists(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_flat_list_of_lists was added")

        _check_plot_design._check_plot_design(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_plot_design was added")

        _check_which_density_gaussian_kernal_plot._check_which_density_gaussian_kernal_plot(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_which_density_gaussian_kernal_plot was added")

        _check_file_name_is_str._check_file_name_is_str(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_file_name_is_str was added")


        winsound.PlaySound('super_mario_finish.wav', winsound.SND_FILENAME)
        print("Done!")


    except:
        print(":(")
        winsound.PlaySound("super_mario_lost_a_life.wav", winsound.SND_FILENAME)
