import json
from collections import defaultdict
import os

# Load JSON files
def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Merge data based on matching 'id'
def merge_data(locations, metadata):
    metadata_dict = {item["id"]: item for item in metadata}
    
    merged_data = []
    for loc in locations:
        loc_id = loc["id"]
        if loc_id in metadata_dict:
            merged_data.append({**loc, **metadata_dict[loc_id]})
        else:
            loc["incomplete_data"] = True
            merged_data.append(loc)  # Mark locations with missing metadata

    return merged_data

# Count valid points per type
def count_by_type(merged_data):
    type_counts = defaultdict(int)
    for loc in merged_data:
        if "type" in loc:
            type_counts[loc["type"]] += 1
    return type_counts

# Calculate average rating per type
def avg_rating_by_type(merged_data):
    type_ratings = defaultdict(list)
    for loc in merged_data:
        if "type" in loc and "rating" in loc:
            type_ratings[loc["type"]].append(loc["rating"])

    return {key: sum(values)/len(values) for key, values in type_ratings.items()}

# Identify location with the highest number of reviews
def highest_reviews_location(merged_data):
    return max(merged_data, key=lambda x: x.get("reviews", 0), default=None)

# Identify incomplete data
def find_incomplete_data(merged_data):
    return [loc for loc in merged_data if "type" not in loc or "rating" not in loc or "reviews" not in loc]

def main():
    # File paths
    base_path = os.path.dirname(os.path.abspath(__file__))
    locations_file = os.path.join(base_path, "../data/locations.json")
    metadata_file = os.path.join(base_path, "../data/metadata.json")

    # Load and process data
    locations = load_json(locations_file)
    metadata = load_json(metadata_file)
    merged_data = merge_data(locations, metadata)

    # Perform analysis
    type_counts = count_by_type(merged_data)
    avg_ratings = avg_rating_by_type(merged_data)
    most_reviewed_location = highest_reviews_location(merged_data)
    incomplete_data = find_incomplete_data(merged_data)

    # Print results
    print("Valid points per type:", type_counts)
    print("Average rating per type:", avg_ratings)
    print("Location with highest reviews:", most_reviewed_location)
    print("Incomplete data locations:", incomplete_data)

if __name__ == "__main__":
    main()
