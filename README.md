# late-show-vincent-clement


This is a Flask-based API for managing episodes, guests, and their appearances on a Late Show. It is designed to track guests, their occupations, the episodes they appear on, and the ratings they receive during their appearances. 

## Project Structure

The project follows a structured approach with the following components:

- **Flask API** to handle requests and perform CRUD operations on the database.
- **SQLAlchemy** for managing the database models and their relationships.
- **Flask-Migrate** to handle database migrations.
- **Postman** collection to test the API endpoints.

## Models

The project defines three primary models:

- **Episode**: Represents an episode of the Late Show.
  - `id`: Unique identifier for the episode.
  - `date`: The date when the episode aired.
  - `number`: The episode number.

- **Guest**: Represents a guest appearing on the show.
  - `id`: Unique identifier for the guest.
  - `name`: Name of the guest.
  - `occupation`: Occupation of the guest (e.g., actor, comedian).

- **Appearance**: Represents an appearance of a guest on a particular episode.
  - `id`: Unique identifier for the appearance.
  - `rating`: A rating (from 1 to 5) given to the appearance.
  - `episode_id`: Foreign key linking to the `Episode`.
  - `guest_id`: Foreign key linking to the `Guest`.

### Relationships:
- An **Episode** has many **Guests** through **Appearance**.
- A **Guest** has many **Episodes** through **Appearance**.
- An **Appearance** belongs to both a **Guest** and an **Episode**.

## License
MIT license 
