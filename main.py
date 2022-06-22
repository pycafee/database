
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


from database.checkers import _check_is_bool, _check_is_data_frame, _check_is_dict, _check_is_float_or_int, _check_list_length, _check_dixon_division_by_zero
from database.checkers import _check_is_float, _check_is_integer, _check_is_list, _check_is_numpy_1_D, _check_array_lower_size
from database.checkers import _check_is_str, _check_data_in_range, _check_is_positive, _check_is_subplots, _check_value_is_equal_or_higher_than, _check_value_is_equal_or_lower_than
from database.distributions import get_shapiro_wilk_tabulated_value, shapiro_wilk, ShapiroWilkNormalityTest, draw_shapiro_wilk_tabulated_values, shapiro_wilk_to_csv, shapiro_wilk_to_xlsx
from database.helpers import _change_locale, _export_to_csv, _check_forbidden_character, _export_to_excel, _check_conflicting_filename, LanguageManagement, AlphaManagement, NDigitsManagement
from database.helpers import _check_blank_space, _sep_checker, _check_figure_extension, _flat_list_of_lists, _check_plot_design, _check_which_density_gaussian_kernal_plot
from database.helpers import _check_file_name_is_str, _check_decimal_separator
from database.functions import multimode
from database.normalitycheck import KolmogorovSmirnov, Lilliefors, AbdiMolin, AndersonDarling, ShapiroWilk, draw_critical_values, normalitycheck_fit_shapiro_wilk
from database.normalitycheck import get_critical_value, to_xlsx, to_csv, normalitycheck_fit, draw_density_function, NormalityCheck, gaussian
from database.sample import Sample, StudentDistribution, Dixon, outliers
from database.generic import generic


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


        KolmogorovSmirnov.KolmogorovSmirnov(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("KolmogorovSmirnov was added")

        _check_is_subplots._check_is_subplots(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_is_subplots was added")






        Lilliefors.Lilliefors(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("Lilliefors was added")

        draw_critical_values.draw_critical_values(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("draw_critical_values was added")

        get_critical_value.get_critical_value(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("get_critical_value was added")

        AbdiMolin.AbdiMolin(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("AbdiMolin was added")

        to_xlsx.to_xlsx(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("to_xlsx was added")

        _check_value_is_equal_or_higher_than._check_value_is_equal_or_higher_than(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_value_is_equal_or_higher_than was added")

        to_csv.to_csv(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("to_csv was added")

        normalitycheck_fit.normalitycheck_fit(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("normalitycheck_fit was added")


        AndersonDarling.AndersonDarling(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("AndersonDarling was added")

        ShapiroWilk.ShapiroWilk(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("ShapiroWilk was added")

        normalitycheck_fit_shapiro_wilk.normalitycheck_fit_shapiro_wilk(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("normalitycheck_fit_shapiro_wilk was added")


        NormalityCheck.NormalityCheck(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("NormalityCheck was added")


        Sample.Sample(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("Sample was added")


        _check_list_length._check_list_length(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_list_length was added")


        StudentDistribution.StudentDistribution(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("StudentDistribution was added")

        _check_array_lower_size._check_array_lower_size(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_array_lower_size was added")

        _check_decimal_separator._check_decimal_separator(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_decimal_separator was added")

        gaussian.gaussian(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("gaussian was added")

        Dixon.Dixon(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("Dixon was added")

        _check_value_is_equal_or_lower_than._check_value_is_equal_or_lower_than(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_value_is_equal_or_lower_than was added")

        generic.generic(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("generic was added")

        outliers.outliers(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("outliers was added")

        _check_dixon_division_by_zero._check_dixon_division_by_zero(database_name)
        winsound.PlaySound('coin.wav', winsound.SND_FILENAME)
        print("_check_dixon_division_by_zero as added")

        winsound.PlaySound('super_mario_finish.wav', winsound.SND_FILENAME)
        print("Done!")


    except:
        print(":(")
        winsound.PlaySound("super_mario_lost_a_life.wav", winsound.SND_FILENAME)
