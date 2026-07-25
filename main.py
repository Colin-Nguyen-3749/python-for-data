from sklearn import tree

# Build a Decision Tree!
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38]]
Y = ['male', 'female', 'female', 'female']

dt = tree.DecisionTreeClassifier()

dt = dt.fit(X,Y)

prediction = clf.predict([190, 70, 43])

print prediction