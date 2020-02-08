from tensorflow import keras
from backend import Vowel_Feature_Train, Vowel_Feature_Test

model = keras.Sequential([
    keras.layers.Conv2D(64, (7, 7), padding='same', input_shape=(20, 16, 1), activation='relu'),
    keras.layers.Conv2D(64, (7, 7), padding='same', activation='relu'),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),

    keras.layers.Conv2D(128, (5, 5), padding='same', activation='relu'),
    keras.layers.Conv2D(128, (5, 5), padding='same', activation='relu'),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),

    keras.layers.Flatten(),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dense(6, activation='softmax')
])

model.compile(optimizer=keras.optimizers.Adam(lr=0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(Vowel_Feature_Train.train_input, Vowel_Feature_Train.train_labels, epochs=6)

results = model.evaluate(Vowel_Feature_Test.test_input, Vowel_Feature_Test.test_labels)
print('test loss, test acc:', results)

model.save('vowel_model.h5', include_optimizer=False)
print("Saved model to disk")
