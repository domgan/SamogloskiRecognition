from tensorflow import keras
import Feature_Train
import Feature_Test

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(20, 47)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(6, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(Feature_Train.train_input, Feature_Train.train_labels, epochs=6)

results = model.evaluate(Feature_Test.test_input, Feature_Test.test_labels)
print('test loss, test acc:', results)

model.save('model.h5')
print("Saved model to disk")
