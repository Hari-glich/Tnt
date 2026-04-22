import matplotlib.pyplot as plt
# students= ["Rohin", "thertha", "adithyan", "chuku", "Arum"]
# scores = [85, 92, 78, 90, 88]
# plt.bar(students, scores, color='blue')
# plt.xlabel('Students')

# plt.ylabel('Scores')
# plt.title('Student Scores')


# plt.show()

#pie chart

# labels = ['Rohin', 'thertha', 'adithyan', 'chuku', 'Arum']
# sizes = [85, 92, 78, 90, 88]
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
# plt.title('Student Scores Distribution')
# plt.axis('equal')
# plt.show()

#scatter plot

x = [85, 92, 78, 90, 88]
y = [1, 2, 3, 4, 5]
plt.scatter(x, y, color='red')
plt.xlabel('Scores')
plt.ylabel('Students')
plt.title('Student Scores Scatter Plot')
plt.grid()
plt.show()