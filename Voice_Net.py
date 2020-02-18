from tensorflow import keras
from preprocessing import Voice_Feature_Train, Voice_Feature_Test

model = keras.Sequential([
    keras.layers.Conv2D(32, (5, 5), padding='same', input_shape=(128, 16, 1), activation='relu'),
    keras.layers.Conv2D(32, (5, 5), padding='same', activation='relu'),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),

    keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
    keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),

    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(2, activation='softmax')
])

model.compile(optimizer=keras.optimizers.Adam(lr=0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(Voice_Feature_Train.train_input, Voice_Feature_Train.train_labels, epochs=3)

results = model.evaluate(Voice_Feature_Test.test_input, Voice_Feature_Test.test_labels)
print('test loss, test acc:', results)

model.save('voice_model.h5', include_optimizer=False)
print("Saved model to disk")
