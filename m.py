from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

data = load_breast_cancer()
X = data.data
y = data.target


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


rf = RandomForestClassifier(n_estimators=100, random_state=0)
rf.fit(X_train, y_train)


accuracy = rf.score(X_test, y_test)
print("Acurácia do modelo:", accuracy)
