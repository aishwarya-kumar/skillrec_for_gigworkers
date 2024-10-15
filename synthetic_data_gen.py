import pandas as pd
import random
import json

tasks = ["Writing", "SEO", "Blogging", "Graphic Design", "Data Entry", "Social Media Management", "Web Development", "UI Design"]

# Define skills for each experience level
skills_by_level = {
    "Writing": {
        "Beginner": ["Basic Writing", "Grammar", "Editing"],
        "Intermediate": ["Creative Writing", "Technical Writing", "Content Strategy"],
        "Advanced": ["Content Marketing", "SEO Writing", "Storytelling"]
    },
    "SEO": {
        "Beginner": ["Keyword Research", "Basic SEO Techniques"],
        "Intermediate": ["Link Building", "On-Page SEO", "Analytics"],
        "Advanced": ["SEO Audits", "Technical SEO", "Advanced Analytics"]
    },
    "Blogging": {
        "Beginner": ["Basic Blogging", "Content Planning"],
        "Intermediate": ["SEO Optimization", "Social Media Promotion"],
        "Advanced": ["Monetization Strategies", "Content Marketing"]
    },
    "Graphic Design": {
        "Beginner": ["Basic Graphic Design", "Color Theory"],
        "Intermediate": ["Adobe Photoshop", "Branding"],
        "Advanced": ["UI/UX Design", "Motion Graphics"]
    },
    "Data Entry": {
        "Beginner": ["Basic Data Entry", "Excel Basics"],
        "Intermediate": ["Data Cleaning", "Database Management"],
        "Advanced": ["Data Analysis", "SQL"]
    },
    "Social Media Management": {
        "Beginner": ["Basic Social Media Skills", "Content Scheduling"],
        "Intermediate": ["Engagement Strategies", "Analytics"],
        "Advanced": ["Advanced Advertising", "Social Media Strategy"]
    },
    "Web Development": {
        "Beginner": ["HTML", "CSS"],
        "Intermediate": ["JavaScript", "Frontend Frameworks"],
        "Advanced": ["Backend Development", "APIs", "DevOps"]
    },
    "UI Design": {
        "Beginner": ["Basic UI Design Principles"],
        "Intermediate": ["Adobe XD", "Figma"],
        "Advanced": ["User Research", "Design Systems"]
    }
}

def generate_gig_worker_profiles(num_workers):
    profiles = []
    for worker_id in range(1, num_workers + 1):
        task_history = random.sample(tasks, random.randint(1, 3))  # Randomly choose 1-3 tasks
        experience_level = random.choice(["Beginner", "Intermediate", "Advanced"])

        # Modify attributes based on experience level
        if experience_level == "Beginner":
            earnings = f"${random.randint(500, 2000)}"
            job_count = random.randint(10, 30)
            time_spent = f"{random.randint(50, 100)} hours"
        elif experience_level == "Intermediate":
            earnings = f"${random.randint(2000, 4000)}"
            job_count = random.randint(30, 70)
            time_spent = f"{random.randint(100, 150)} hours"
        else:  # Advanced
            earnings = f"${random.randint(4000, 8000)}"
            job_count = random.randint(70, 120)
            time_spent = f"{random.randint(150, 250)} hours"

        rating = round(random.uniform(3.5, 5.0), 1)  # Random rating between 3.5 and 5.0
        current_skills = ", ".join([skill for skill in skills_by_level.keys() if skill in task_history])

        # Generate recommended skills based on task history and experience level
        recommended_skills_set = set()
        for task in task_history:
            recommended_skills_set.update(skills_by_level[task][experience_level])

        # Create a string of recommended skills
        recommended_skills = ", ".join(recommended_skills_set)

        # Append profile in a format suitable for training the LLM
        profile = {
            "input": {
                "Worker ID": worker_id,
                "Task History": ", ".join(task_history),
                "Earnings": earnings,
                "Rating": rating,
                "Current Skills": current_skills,
                "Experience Level": experience_level,
                "Job Count": job_count,
                "Time Spent on Gigs": time_spent
            },
            "output": {
                "Recommended Skills": recommended_skills
            }
        }
        profiles.append(profile)

    return profiles


# Generate gig worker profiles
gig_worker_profiles = generate_gig_worker_profiles(50)
# for profile in gig_worker_profiles:
#     print(profile)

# gig_worker_profiles = pd.DataFrame(gig_worker_profiles)
# gig_worker_profiles.to_csv("gig_workers_synthdata.csv")
with open('gig_workers_synthdata.json', 'w') as json_file:
    json.dump(gig_worker_profiles, json_file, indent=4)

skills = ["Writing", "SEO", "Graphic Design", "Branding", "Data Entry", "Admin Support", "Social Media Management",
          "Web Development", "UI Design"]
platforms = ["Coursera", "Udemy", "LinkedIn Learning", "edX", "Skillshare", "Khan Academy", "Google Digital Garage"]

# Define some random price ranges, durations, and difficulty levels
price_ranges = ["Free", "$50", "$100", "$200"]
durations = ["2 hours", "5 hours", "10 hours", "1 week", "2 weeks", "3 weeks", "1 month"]
difficulty_levels = ["Beginner", "Intermediate", "Advanced"]

# Define resource types
resource_types = ["Course", "Certification", "Tutorial", "Workshop"]

# Function to generate training resources
def generate_training_resources(num_resources):
    training_resources = []

    for resource_id in range(1, num_resources + 1):
        skill = random.choice(skills)
        platform = random.choice(platforms)
        resource_type = random.choice(resource_types)
        difficulty = random.choice(difficulty_levels)
        price = random.choice(price_ranges)
        duration = random.choice(durations)
        url = f"https://www.{platform.lower().replace(' ', '')}.com/{skill.lower().replace(' ', '-')}-course-{resource_id}"

        resource = {
            "Resource ID": resource_id,
            "Skill": skill,
            "Resource Type": resource_type,
            "Platform": platform,
            "Difficulty Level": difficulty,
            "Price": price,
            "Duration": duration,
            "URL": url
        }

        training_resources.append(resource)

    return training_resources


# Generate 10 sample training resources
training_resources = generate_training_resources(50)
# for resource in training_resources:
#     print(resource)

# training_resources = pd.DataFrame(training_resources)
# training_resources.to_csv("training_res_synthdata.csv")
with open('training_res_synthdata.json', 'w') as json_file:
    json.dump(training_resources, json_file, indent=4)