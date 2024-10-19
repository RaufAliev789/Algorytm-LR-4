class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_stack = []
        self.max_size = max_size  # Устанавливаем максимальный размер стека

    def push(self, value):
        if len(self.stack) >= self.max_size:  # ПРЕДВАРИТЕЛЬНАЯ  проверка на переполнение
            return "Ошибка: стек переполнен"

        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:  # (последний = верхний в стеке)
            self.max_stack.append(value)

    def pop(self):
        if not self.stack:  # ПРЕДВАРИТЕЛЬНАЯ gроверка на пустоту стека
            return None

        popped_value = self.stack.pop()  # удаляем из 2 СТЕКОВ
        if popped_value == self.max_stack[-1]:
            self.max_stack.pop()
        return popped_value

    def max(self):
        if not self.max_stack:  # ПРЕДВАРИТЕЛЬНАЯ проверка на пустоту стека
            return None
        return self.max_stack[-1]

    def remove(self, value):
        if value in self.stack:
            temp_stack = []
            # Переносим элементы в временный стек, пока не найдем нужный
            while self.stack:
                popped_value = self.stack.pop()
                if popped_value == value:
                    break  # ПРОХОД по всем элементам, удаление всех элементов и добавление удаленных во временный стек. КРОМЕ ИСКОМОГО
                temp_stack.append(popped_value)

            # Возвращаем элементы обратно в основной стек
            while temp_stack:
                self.push(temp_stack.pop())

            # Обновляем max_stack (если из общего стека эл больше последнего максимума, то добавляем)
            self.max_stack = []
            for item in self.stack:
                if not self.max_stack or item >= self.max_stack[-1]:
                    self.max_stack.append(item)


if __name__ == "__main__":
    q = int(input("Введите количество запросов: "))  # Читаем количество запросов
    max_size = int(input("Введите максимальный размер стека: "))  # Читаем максимальный размер
    stk = Stack(max_size)

    for _ in range(q):
        command = input().strip().split()  # Читаем команду

        if command[0] == "push":  # 0 = push 1 = элемент число
            value = int(command[1])
            result = stk.push(value)
            if result:
                print(result)  # Выводим сообщение об ошибке, если стек переполнен
        elif command[0] == "pop":
            stk.pop()
        elif command[0] == "max":
            current_max = stk.max()
            if current_max is not None:
                print(current_max)
        elif command[0] == "remove":
            value = int(command[1])
            stk.remove(value)
