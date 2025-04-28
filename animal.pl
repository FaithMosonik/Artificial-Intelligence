% Animal Classification System
% Animal Characteristics

has_property(mammal, warm_blooded).
has_property(mammal, hair_or_fur).
has_property(mammal, milk).
has_property(bird, warm_blooded).
has_property(bird, feathers).
has_property(bird, lays_eggs).
has_property(reptile, cold_blooded).
has_property(reptile, scales).
has_property(reptile, lays_eggs).


% Animal Classifications

is_a(dog, mammal).
is_a(cat, mammal).
is_a(bat, mammal).
is_a(eagle, bird).
is_a(penguin, bird).
is_a(snake, reptile).
is_a(lizard, reptile).

% Specific Properties

has_property(dog, barks).
has_property(cat, meows).
has_property(bat, flies).
has_property(eagle, flies).
has_property(penguin, swims).
has_property(snake, no_limbs).

% Rules

% An animal has a property if it has it directly
animal_has_property(Animal, Property) :-
    has_property(Animal, Property).

% An animal has a property if its class has that property
animal_has_property(Animal, Property) :-
    is_a(Animal, Class),
    has_property(Class, Property).

% Find all animals with a specific property
animals_with_property(Property, Animals) :-
    findall(Animal, animal_has_property(Animal, Property), Animals).

% Classify a known animal based on its classification
classify(Animal, Class) :-
    is_a(Animal, Class).

% ---------------------------
% Program Entry Point
% ---------------------------

:- initialization(main).

main :-
    write('Hello, World!'), nl.
