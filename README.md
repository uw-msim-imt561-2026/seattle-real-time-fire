# seattle-real-time-fire

## Submission Details
- **Streamlit deployed link:** https://imt561-2025-seattle-real-time-fire.streamlit.app/
- **Github Repo Link:** https://github.com/uw-msim-imt561-2026/seattle-real-time-fire

## Audience
The primary stakeholders for this dashboard are leadership within the Seattle Fire Department, emergency dispatch managers,
and city-level public safety planners in Seattle. Although these groups operate at different organizational levels, they 
share a common objective: allocating resources in a way that maximizes public safety while maintaining operational efficiency.
Dispatch managers focus on short-term, day-to-day operational decisions. Their concerns include how to distribute calls 
across stations, how to anticipate peak demand periods, and how to minimize response times under capacity constraints. 
Fire department leadership operates at a broader tactical and strategic level, making decisions about staffing levels, 
seasonal shift adjustments, station readiness, and long-term expansion. City public safety planners view the data from a 
policy and budgeting perspective, seeking to understand citywide trends in emergency activity in order to guide funding 
decisions, identify recurring risk areas, and support long-term emergency preparedness strategies.

## Dataset
The dataset consists of real-time 911 fire and emergency incidents handled by the Seattle Fire Department during 2025. 
Each row represents a single dispatched incident and includes timestamped information describing when the call occurred, 
the type of emergency, and its geographic location. The data was manually filtered prior to download to focus specifically 
on 2025 incidents, ensuring time-related consistency for analysis. Because the dataset is event-level and time-stamped, 
it is well-suited for exploratory and time-series analysis. It enables examination of call volume patterns by hour, day, 
month, and season, as well as geographic clustering of incidents across the city. Additionally, the structure of the data 
provides a reliable snapshot of operational demand placed on emergency services and serves as a foundation for identifying 
recurring patterns, concentrations of activity, and variation in emergency types over time.

## Context
The context of this analysis centers on improving resource allocation and decision-making within Seattle’s public safety infrastructure. 
Key analytical questions guiding the dashboard design include:
1) How does call volume change by time of day, day of week, or season?
2) Which areas of the city consistently generate higher volumes of incidents, and are certain locations associated with 
specific emergency types?
3) Are there observable trends in incident types over time that could inform staffing, budgeting, or prevention strategies?

