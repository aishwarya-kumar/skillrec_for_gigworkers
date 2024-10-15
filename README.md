# Leveraging-LLMs-to-provide-skill-suggestions-and-recommendations for gig workers

**Project plan:**

**Scope:** 
Analyze gig workers' task histories and leverage LLMs to generate personalized skill suggestions. Use RAG to retrieve relevant training resources.

**Key Research Questions:**
1.	How can LLMs analyze a gig worker’s task history to provide personalized career advice?
2.	How effective is RAG in retrieving relevant skill-development resources (e.g., courses, certifications)?
3.	What impact does this guidance have on workers’ satisfaction and earnings?

**Literature review:** 
Study existing AI applications for skill development and personalized recommendations, analyze research on AI-based tools for gig workers, such as GigSense. (I am also reading through work done in the lab and work Kashif has done in the past)

**Data collection:** 
Scraping data from Upwork to get user profiles, job types, earnings, ratings, and completion times. Collecting information on what skills are valued in specific types of gigs and what certifications, courses, or experiences lead to higher-paying jobs. Need to find curated resources such as job training websites, online courses and certification programs- maybe an API for Coursera

**Implementation:**
- Build the recommendation engine to suggest skills based on task history, job trends, and worker preferences.
- Fine-tune the LLM using gig worker-related data to ensure accurate skill recommendations.
- Implement the RAG system to pull up-to-date resources from online platforms (MOOCs, certification sites) based on the recommended skills.

If possible, test with a small group of gig workers to assess the accuracy and usefulness of the skill recommendations.
