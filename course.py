# James McGowan September 17, 2024
# combines various golf courses to create a single one.
# there will be three different courses for each part: tee box, landscape, and green.
# courses can I either follow an American structure, or European.

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

REGIONS = ['American', 'European']

TEE_BOXES = {
    'American': ["Buffalo Ridge", "Congressional", "Wells Fargo"],
    'European': ["Royal Troon", "Le Golf National", "Marco Simone"]
}

LANDSCAPES = {
    'American': ["Saguaro", "Whistling Straits", "Harbour Town"],
    'European': ["Royal County Down", "West Cliffs" , "St. Andrews"]  
}

GREENS = {
    'American': ["TPC Sawgrass", "Augusta National", "Pebble Beach"],
    'European': ["Les Bordes", "Royal Liverpool", "Valderrama"]  
}

class courseMaker:
    def __init__(self, landscape_matrix, green_matrix, regions, tee_boxes, landscapes, greens):
        self.landscape_matrix = landscape_matrix
        self.green_matrix = green_matrix
        self.regions = regions
        self.tee_boxes = tee_boxes
        self.landscapes = landscapes
        self.greens = greens

    def get_tee_box(self):
        self.region = np.random.choice(self.regions)
        return np.random.choice(self.tee_boxes[self.region])

    def get_landscape(self, current_course):
        landscape_options = self.landscapes[self.region]
        transition_probs = [self.landscape_matrix[self.region][current_course][next_course] for next_course in landscape_options]
        return np.random.choice(landscape_options, p=transition_probs)

    def get_green(self, current_course):
        green_options = self.greens[self.region]
        transition_probs = [self.green_matrix[self.region][current_course][next_course] for next_course in green_options]
        return np.random.choice(green_options, p=transition_probs)

    def course_sequence(self):
        tee_box = self.get_tee_box()
        landscape = self.get_landscape(tee_box)
        green = self.get_green(landscape)

        return [self.region, tee_box, landscape, green]

def main():
    # Probabilities that a lanscape will be chosen (based on the tee boxes)
    landscape_matrix = {
        'American': {
            "Buffalo Ridge": {"Saguaro": 0.4, "Whistling Straits": 0.3, "Harbour Town": 0.3},
            "Congressional": {"Saguaro": 0.2, "Whistling Straits": 0.5, "Harbour Town": 0.3},
            "Wells Fargo": {"Saguaro": 0.25, "Whistling Straits": 0.4, "Harbour Town": 0.35}
        },
        'European': {
            "Royal Troon": {"Royal County Down": 0.3, "West Cliffs": 0.4, "St. Andrews": 0.3},
            "Le Golf National": {"Royal County Down": 0.35, "West Cliffs": 0.3, "St. Andrews": 0.35},
            "Marco Simone": {"Royal County Down": 0.25, "West Cliffs": 0.35, "St. Andrews": 0.4}
        }
    }

    # Probabilities that a green will be chosen (based on the landscape)
    green_matrix = {
        'American': {
            "Saguaro": {"TPC Sawgrass": 0.4, "Augusta National": 0.35, "Pebble Beach": 0.25},
            "Whistling Straits": {"TPC Sawgrass": 0.2, "Augusta National": 0.5, "Pebble Beach": 0.3},
            "Harbour Town": {"TPC Sawgrass": 0.6, "Augusta National": 0.1, "Pebble Beach": 0.3}
        },
        'European': {
            "Royal County Down": {"Les Bordes": 0.3, "Royal Liverpool": 0.4, "Valderrama": 0.3},
            "West Cliffs": {"Les Bordes": 0.35, "Royal Liverpool": 0.3, "Valderrama": 0.35},
            "St. Andrews": {"Les Bordes": 0.25, "Royal Liverpool": 0.35, "Valderrama": 0.4}
        }
    }

    course_maker = courseMaker(
        landscape_matrix,
        green_matrix,
        REGIONS,
        TEE_BOXES,
        LANDSCAPES,
        GREENS
    )

    new_course = course_maker.course_sequence()

    # American tee boxes
    buffalo_ridge = Image.open("buffalo_ridge.jpeg").resize((200, 150))
    congressional = Image.open("congressional.jpeg").resize((200, 150))
    wells_fargo = Image.open("wells_fargo.jpeg").resize((200, 150))

    # European tee boxes
    royal_troon = Image.open("royal_troon.jpeg").resize((200, 150))
    le_golf_national = Image.open("le_golf_national.jpeg").resize((200, 150))
    marco_simone = Image.open("marco_simone.jpeg").resize((200, 150))

    # American landscapes
    saguaro = Image.open("saguaro.jpeg").resize((200, 150))
    whistling_straits = Image.open("whistling_straits.jpeg").resize((200, 150))
    harbour_town = Image.open("harbour_town.jpeg").resize((200, 150))

    # European landscapes
    royal_county_down = Image.open("royal_county_down.jpeg").resize((200, 150))
    west_cliffs = Image.open("west_cliffs.jpeg").resize((200, 150))
    st_andrews = Image.open("st_andrews.jpeg").resize((200, 150))

    # American greens
    tpc_sawgrass = Image.open("tpc_sawgrass.jpeg").resize((200, 150))
    augusta_national = Image.open("augusta_national.jpeg").resize((200, 150))
    pebble_beach = Image.open("pebble_beach.jpeg").resize((200, 150))

    # European greens
    les_bordes = Image.open("les_bordes.jpeg").resize((200, 150))
    valderrama = Image.open("valderrama.jpeg").resize((200, 150))
    royal_liverpool = Image.open("royal_liverpool.jpeg").resize((200, 150))

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 4))
    x_values = np.arange(3)

    # Mapping of course names to image objects
    course_images = {
        # American tee boxes
        "Buffalo Ridge": buffalo_ridge,
        "Congressional": congressional,
        "Wells Fargo": wells_fargo,
        # European tee boxes
        "Royal Troon": royal_troon,
        "Le Golf National": le_golf_national,
        "Marco Simone": marco_simone,
        # American landscapes
        "Saguaro": saguaro,
        "Whistling Straits": whistling_straits,
        "Harbour Town": harbour_town,
        # European landscapes
        "Royal County Down": royal_county_down,
        "West Cliffs": west_cliffs,
        "St. Andrews": st_andrews,
        # American greens
        "TPC Sawgrass": tpc_sawgrass,
        "Augusta National": augusta_national,
        "Pebble Beach": pebble_beach,
        # European greens
        "Les Bordes": les_bordes,
        "Valderrama": valderrama,
        "Royal Liverpool": royal_liverpool
    }

    # Display each image in the corresponding position (skip the region in new_course)
    for i, course in enumerate(new_course[1:]):  # Skip the region
        ax.imshow(course_images[course], extent=[i - 0.45, i + 0.45, -0.4, 0.4], aspect='equal')

    # Adjusting the axis properties
    ax.set_xlim(-0.5, 2.5)  # Fits the number of images (3)
    ax.set_ylim(-1, 1)
    ax.set_xticks(x_values)
    ax.set_xticklabels(new_course[1:])  # Skip the region in labels
    ax.set_yticks([])
    ax.set_title(f"{new_course[0]}-Style Golf Course ")

    plt.show()

if __name__ == "__main__":
    main()