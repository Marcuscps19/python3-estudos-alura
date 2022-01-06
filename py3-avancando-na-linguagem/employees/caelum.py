from employee import Employee


class Caelum(Employee):
    def show_tasks(self):
        print('Fez muita coisa, Caelumer')

    def search_courses_of_month(self, month=None):
        print(f'Mostrando cursos - {month}'
              if month
              else 'Mostrando cursos desse mês')
