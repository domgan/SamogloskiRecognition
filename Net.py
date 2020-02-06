from tensorflow import keras
import Feature_Train
import Feature_Test

model = keras.Sequential([
    keras.layers.Conv2D(128, (3, 3), input_shape=(20, 16, 1), activation='relu'),
    keras.layers.Conv2D(128, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),

    keras.layers.Conv2D(256, (3, 3), activation='relu'),
    keras.layers.Conv2D(256, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),

    keras.layers.Flatten(),
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dense(6, activation='softmax')
    ])

model.compile(optimizer=keras.optimizers.Adam(lr=0.0001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(Feature_Train.train_input, Feature_Train.train_labels, epochs=5)

results = model.evaluate(Feature_Test.test_input, Feature_Test.test_labels)
print('test loss, test acc:', results)

model.save('model.h5')
print("Saved model to disk")
