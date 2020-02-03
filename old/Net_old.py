from tensorflow import keras
import Feature_Train_old as Feature_Train
import Feature_Test_old as Feature_Test

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(20, 32)),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dense(6, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(Feature_Train.train_input, Feature_Train.train_labels, epochs=5)

results = model.evaluate(Feature_Test.test_input, Feature_Test.test_labels)
print('test loss, test acc:', results)

model.save('model.h5')
print("Saved model to disk")
