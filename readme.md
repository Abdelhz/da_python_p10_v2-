# Softdesk Project

## English


Softdesk is a Django REST Framework application (API) that allows users to manage projects and issues.

## Maine functionalities

- Create, read, update and delete users
- Create, read, update and delete projects.
- Create, read, update and delete contributors for those projects.
- Create, read, update and delete issues for those projects.
- Create, read, update and delete comments for those issues.


## Setup

1. Create a project folder named "project_10_django_rest_framework":

    ```bash
    mkdir project_10_django_rest_framework
    ```

2. Navigate into the folder:

    ```bash
    cd project_10_django_rest_framework
    ```

3. Clone the project from GitHub into this folder:

    ```bash
    git clone https://github.com/Abdelhz/da_python_p10_v2.git
    ```

4. Navigate into the cloned project's directory "da_python_p10_v2":

    ```bash
    cd da_python_p10_v2
    ```

5. Create a virtual environment:

    ```bash
    python3 -m venv env_django_rest_project
    ```

6. Activate the virtual environment:
    - On Windows:

        ```bash
        cd env_django_rest_project/Scripts/
        ```

        ```bash
        source activate
        ```

        ```bash
        cd ../../
        ```

    - On Unix or MacOS:

        ```bash
        source env/bin/activate
        ```

7. Install the dependencies from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

8. Navigate to the directory where `manage.py` is located:

    ```bash
    cd da_python_p10_v2/softdesk
    ```

9. Start the Django rest Api project:

    ```bash
    python manage.py runserver
    ```

The project functionalities are usable through endpoints. Those endpoints are to be tested in postman or using "curl" on a terminal.

## Endpoints

### login

- `POST http://127.0.0.1:8000/login/`: obtain a jwt (json web token) using credentials of an existing user.

### Authentication

- After obtaining the jwt, use it in every endpoint of the following list by putting it in the "headers" field :

#### "headers"

1. key: "Authorization"
2. value: "Bearer ('jwt token')"

- For POST, PATCH or PUT request add to the "headers" :

1. key: "Content-Type"
2. value: "application/json"

    Sample JSON:

    ```json
    {
        "username": "Username",
        "password": "securepassword"
    }
    ```

### Users

- `GET http://127.0.0.1:8000/users/`: List all users.
- `POST http://127.0.0.1:8000/users/`: Create a new user.

    Sample JSON:

    ```json
    {
        "username": "username",
        "first_name": "first_name",
        "last_name": "last_name",
        "date_of_birth": "YYYY-MM-DD",
        "email": "email@example.com",
        "password": "password"
    }
    ```

- `GET http://127.0.0.1:8000/users/{id}/`: Retrieve a specific user.
- `PUT or PATCH http://127.0.0.1:8000/users/{id}/`: Update a specific user.

    Sample JSON:

    ```json
    {
        "username": "username",
        "first_name": "first_name",
        "last_name": "last_name",
        "date_of_birth": "YYYY-MM-DD",
        "email": "email@example.com",
        "password": "password"
    }
    ```

- `DELETE http://127.0.0.1:8000/users/{id}/`: Delete a specific user.

### Projects

- `GET http://127.0.0.1:8000/projects/`: List all projects.
- `POST http://127.0.0.1:8000/projects/`: Create a new project.

    Sample JSON:

    ```json
    {
        "title": "Project Title",
        "description": "Project Description",
        "type": "Project Type",
    }
    ```

- `GET http://127.0.0.1:8000/projects/{id}/`: Retrieve a specific project.
- `PUT or PATCH http://127.0.0.1:8000/projects/{id}/`: Update a specific project.

    Sample JSON:

    ```json
    {
        "title": "modified Project Title",
        "description": "modified Project Description",
        "type": "modified Project Type",

    }
    ```

- `DELETE http://127.0.0.1:8000/projects/{id}/`: Delete a specific project.

### Contributors

- `GET http://127.0.0.1:8000/projects/{id}/contributors/`: List all contributors to a specific project.
- `POST http://127.0.0.1:8000/projects/{id}/contributors/`: Create a new contributor to a specific project.

    Sample JSON:

    ```json
    {
        "user": "user_id",
        "role": "contributor",
        "permission": "can_edit/can_view/can_delete",
        "can_assign_issues": true or false
    }
    ```

- `GET http://127.0.0.1:8000/projects/{id}/contributors/{id}/`: Retrieve a specific contributor.
- `PUT or PATCH http://127.0.0.1:8000/projects/{id}/contributors/{id}/`: Update a specific contributor.

    Sample JSON:

    ```json
    {
        "can_assign_issues": false
    }
    ```

- `DELETE http://127.0.0.1:8000/projects/{id}/contributors/{id}/`: Delete a specific contributor.

### Issues

- `GET http://127.0.0.1:8000/projects/{project_id}/issues/`: List all issues for a specific project.
- `POST http://127.0.0.1:8000/projects/{project_id}/issues/`: Create a new issue for a specific project.

    Sample JSON:

    ```json
    {
        "title": "Issue Title",
        "description": "Issue Description",
        "tag": "Issue Tag",
        "priority": "Issue Priority",
        "status": "Issue Status",
        "assignee": "assignee contributor's ID"
    }
    ```

- `GET http://127.0.0.1:8000/projects/{project_id}/issues/{id}/`: Retrieve a specific issue for a specific project.
- `PUT or PATCH http://127.0.0.1:8000/projects/{project_id}/issues/{id}/`: Update a specific issue for a specific project.

    Sample JSON:

    ```json
    {
        "title": "New Issue Title",
        "description": "New Issue Description",
        "tag": "New Issue Tag",
        "priority": "New Issue Priority",
        "status": "New Issue Status",
        "assignee": "New assignee contributor's ID"
    }
    ```

- `DELETE http://127.0.0.1:8000/projects/{project_id}/issues/{id}/`: Delete a specific issue for a specific project.

### Comments

- `GET http://127.0.0.1:8000/projects/{project_id}/issues/{issue_id}/comments/`: List all comments for a specific issue.
- `POST http://127.0.0.1:8000/projects/{project_id}/issues/{issue_id}/comments/`: Create a new comment for a specific issue.

    Sample JSON:

    ```json
    {
        "description": "Comment Description"
    }
    ```

- `GET http://127.0.0.1:8000/projects/{project_id}/issues/{issue_id}/comments/{id}/`: Retrieve a specific comment for a specific issue.
- `PUT or PATCH http://127.0.0.1:8000/projects/{project_id}/issues/{issue_id}/comments/{id}/`: Update a specific comment for a specific issue.

    Sample JSON:

    ```json
    {
        "description": "New Comment Description"
    }
    ```

- `DELETE http://127.0.0.1:8000/projects/{project_id}/issues/{issue_id}/comments/{id}/`: Delete a specific comment for a specific issue.

## Project applications

[Some details about the views, URLs, and permissions of the Issues app]

### Users App

The Users app includes a `CustomUser` model that extends the built-in `AbstractUser` model. The `CustomUser` model includes additional fields like `date_of_birth`, `can_be_contacted`, `can_data_be_shared`, `created_time`, and `updated_time`.

The app also includes a `IsOwnerOrReadOnly` permission class that only allows owners of an object to edit it.

The URL routes for the Users app include routes for the root of the app, as well as a signup route. The root route uses a router to automatically generate routes for the `CustomUserViewSet`.

The `CustomUserViewSet` allows users to be viewed or edited. The viewset includes custom logic for creating a user and for determining the permissions for different actions.

The `CustomUserSerializer` includes validation logic to ensure that users are at least 15 years old.

### Projects App

The Projects app is responsible for managing the projects within the application. It includes the `Project` and `Contributor` models.

The `Project` model represents a project within the application. Each project has a title, description, and type.

The `Contributor` model represents a user who is a contributor to a project. Each contributor has a role, permission, and a flag indicating whether they can assign issues.

The app includes the `ProjectViewSet` and `ContributorViewSet` for handling the CRUD operations related to projects and contributors respectively.

The `ProjectSerializer` and `ContributorSerializer` are used for serializing and deserializing the project and contributor instances.

The app also includes custom permissions classes like `IsProjectOwnerOrReadOnly` and `IsContributorOrReadOnly` to handle object-level permissions.

The URL routes for the Projects app include routes for listing all projects, retrieving a specific project, updating a project, deleting a project, listing all contributors of a project, adding a contributor to a project, updating a contributor, and removing a contributor from a project.

### Issues App

The Issues app is responsible for managing the issues within the application. It includes the `Issue` model.

The `Issue` model represents an issue within a project. Each issue has a title, description, tag, priority, project, status, author, and assignee.

The app includes the `IssueViewSet` for handling the CRUD operations related to issues.

The `IssueSerializer` is used for serializing and deserializing the issue instances.

The app also includes custom permissions classes like `IsAuthorOrReadOnly` to handle object-level permissions.

The URL routes for the Issues app include routes for listing all issues, retrieving a specific issue, updating an issue, and deleting an issue.

### Comments App

The Comments app is responsible for managing the comments within the application. It includes the `Comment` model.

The `Comment` model represents a comment on an issue. Each comment has a description, author, and issue.

The app includes the `CommentViewSet` for handling the CRUD operations related to comments.

The `CommentSerializer` is used for serializing and deserializing the comment instances.

The app also includes custom permissions classes like `IsAuthorOrReadOnly` to handle object-level permissions.

The URL routes for the Comments app include routes for listing all comments, retrieving a specific comment, updating a comment, and deleting a comment.

## FRANÇAIS

Softdesk est une application Django REST Framework (API) permettant aux utilisateurs de gérer des projets et des problèmes.

## Fonctionnalités principales

- Créer, lire, mettre à jour et supprimer des utilisateurs
- Créer, lire, mettre à jour et supprimer des projets.
- Créer, lire, mettre à jour et supprimer des contributeurs pour ces projets.
- Créer, lire, mettre à jour et supprimer des problèmes pour ces projets.
- Créer, lire, mettre à jour et supprimer des commentaires pour ces problèmes.

## Configuration

1. Créer un dossier de projet nommé "project_10_django_rest_framework":

    ```bash
    mkdir project_10_django_rest_framework
    ```

2. Naviguer dans le dossier:

    ```bash
    cd project_10_django_rest_framework
    ```

3. Cloner le projet depuis GitHub dans ce dossier:

    ```bash
    git clone https://github.com/Abdelhz/da_python_p10_v2.git
    ```

4. Naviguer dans le répertoire du projet cloné "da_python_p10_v2":

    ```bash
    cd da_python_p10_v2
    ```

5. Créer un environnement virtuel:

    ```bash
    python3 -m venv env_django_rest_project
    ```

6. Activer l'environnement virtuel:
    - Sur Windows:

        ```bash
        cd env_django_rest_project/Scripts/
        ```

        ```bash
        source activate
        ```

        ```bash
        cd ../../
        ```

    - Sur Unix ou MacOS:

        ```bash
        source env/bin/activate
        ```

7. Installer les dépendances à partir du fichier `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

8. Naviguer dans le répertoire où se trouve `manage.py`:

    ```bash
    cd da_python_p10_v2/softdesk
    ```

9. Démarrer le projet Django rest Api:

    ```bash
    python manage.py runserver
    ```

Les fonctionnalités du projet sont utilisables via des points d'extrémité (endpoints). Ces points d'extrémité sont à tester dans Postman ou en utilisant "curl" dans un terminal.

## Points de terminaison (Endpoints)

### Connexion

- `POST http://127.0.0.1:8000/login/`: obtenir un jwt (jeton web JSON) en utilisant les informations d'identification d'un utilisateur existant.

### Authentification

- Après avoir obtenu le jwt, utilisez-le dans chaque point d'extrémité de la liste suivante en le plaçant dans le champ "headers" :

#### "headers"

1. clé: "Authorization"
2. valeur: "Bearer ('jeton jwt')"

- Pour une requête POST, PATCH ou PUT, ajoutez au "headers" :

1. clé: "Content-Type"
2. valeur: "application/json"

    Exemple JSON:

    ```json
    {
        "username": "NomUtilisateur",
        "password": "motdepassesecure"
    }
    ```

### Utilisateurs

- `GET http://127.0.0.1:8000/users/`: Liste tous les utilisateurs.
- `POST http://127.0.0.1:8000/users/`: Crée un nouvel utilisateur.

    Exemple JSON:

    ```json
    {
        "username": "nomutilisateur",
        "first_name": "prenom",
        "last_name": "nomdefamille",
        "date_of_birth": "AAAA-MM-JJ",
        "email": "email@example.com",
        "password": "motdepasse"
    }
    ```

- `GET http://127.0.0.1:8000/users/{id}/`: Récupère un utilisateur spécifique.
- `PUT or PATCH http://127.0.0.1:8000/users/{id}/`: Met à jour un utilisateur spécifique.

    Exemple JSON:

    ```json
    {
        "username": "nomutilisateur",
        "first_name": "prenom",
        "last_name": "nomdefamille",
        "date_of_birth": "AAAA-MM-JJ",
        "email": "email@example.com",
        "password": "motdepasse"
    }
    ```

- `DELETE http://127.0.0.1:8000/users/{id}/`: Supprime un utilisateur spécifique.

### Projets

- `GET http://127.0.0.1:8000/projects/`: Liste tous les projets.
- `POST http://127.0.0.1:8000/projects/`: Crée un nouveau projet.

    Exemple JSON:

    ```json
    {
        "title": "Titre du projet",
        "description": "Description du projet",
        "type": "Type de projet",
    }
    ```

- `GET http://127.0.0.1:8000/projects/{id}/`: Récupère un projet spécifique.
- `PUT or PATCH http://127.0.0.1:8000/projects/{id}/`: Met à jour un projet spécifique.

    Exemple JSON:

    ```json
    {
        "title": "Titre du projet modifié",
        "description": "Description du projet modifiée",
        "type": "Type de projet modifié",

    }
    ```

- `DELETE http://127.0.0.1:8000/projects/{id}/`: Supprime un projet spécifique.

### Contributeurs

- `GET http://127.0.0.1:8000/projects/{id}/contributors/`: Liste tous les contributeurs d'un projet spécifique.
- `POST http://127.0.0.1:8000/projects/{id}/contributors/`: Crée un nouveau contributeur pour un projet spécifique.

    Exemple JSON:

    ```json
    {
        "user": "id_utilisateur",
        "role": "contributeur",
        "permission": "peut_editer/peut_voir/peut_supprimer",
        "can_assign_issues": true ou false
    }
    ```

- `GET http://127.0.0.1:8000/projects/{id}/contributors/{id}/`: Récupère un contributeur spécifique.
- `PUT or PATCH http://127.0.0.1:8000/projects/{id}/contributors/{id}/`: Met à jour un contributeur spécifique.

    Exemple JSON:

    ```json
    {
        "can_assign_issues": false
    }
    ```

- `DELETE http://127.0.0.1:8000/projects/{id}/contributors/{id}/`: Supprime un contributeur spécifique.

### Problèmes

- `GET http://127.0.0.1:8000/projects/{id_projet}/issues/`: Liste tous les problèmes d'un projet spécifique.
- `POST http://127.0.0.1:8000/projects/{id_projet}/issues/`: Crée un nouveau problème pour un projet spécifique.

    Exemple JSON:

    ```json
    {
        "title": "Titre du problème",
        "description": "Description du problème",
        "tag": "Étiquette du problème",
        "priority": "Priorité du problème",
        "status": "Statut du problème",
        "assignee": "ID du contributeur assigné"
    }
    ```

- `GET http://127.0.0.1:8000/projects/{id_projet}/issues/{id}/`: Récupère un problème spécifique pour un projet spécifique.
- `PUT or PATCH http://127.0.0.1:8000/projects/{id_projet}/issues/{id}/`: Met à jour un problème spécifique pour un projet spécifique.

    Exemple JSON:

    ```json
    {
        "title": "Nouveau titre du problème",
        "description": "Nouvelle description du problème",
        "tag": "Nouvelle étiquette du problème",
        "priority": "Nouvelle priorité du problème",
        "status": "Nouveau statut du problème",
        "assignee": "Nouvel ID du contributeur assigné"
    }
    ```

- `DELETE http://127.0.0.1:8000/projects/{id_projet}/issues/{id}/`: Supprime un problème spécifique pour un projet spécifique.

### Commentaires

- `GET http://127.0.0.1:8000/projects/{id_projet}/issues/{id_probleme}/comments/`: Liste tous les commentaires pour un problème spécifique.
- `POST http://127.0.0.1:8000/projects/{id_projet}/issues/{id_probleme}/comments/`: Crée un nouveau commentaire pour un problème spécifique.

    Exemple JSON:

    ```json
    {
        "description": "Description du commentaire"
    }
    ```

- `GET http://127.0.0.1:8000/projects/{id_projet}/issues/{id_probleme}/comments/{id}/`: Récupère un commentaire spécifique pour un problème spécifique.
- `PUT or PATCH http://127.0.0.1:8000/projects/{id_projet}/issues/{id_probleme}/comments/{id}/`: Met à jour un commentaire spécifique pour un problème spécifique.

    Exemple JSON:

    ```json
    {
        "description": "Nouvelle description du commentaire"
    }
    ```

- `DELETE http://127.0.0.1:8000/projects/{id_projet}/issues/{id_probleme}/comments/{id}/`: Supprime un commentaire spécifique pour un problème spécifique.

## Applications du projet

### Application Utilisateurs

L'application Utilisateurs comprend un modèle `CustomUser` qui étend le modèle intégré `AbstractUser`. Le modèle `CustomUser` inclut des champs supplémentaires tels que `date_of_birth`, `can_be_contacted`, `can_data_be_shared`, `created_time` et `updated_time`.

L'application comprend également une classe de permission `IsOwnerOrReadOnly` qui permet uniquement aux propriétaires d'un objet de le modifier.

Les routes URL pour l'application Utilisateurs comprennent des routes pour la racine de l'application, ainsi qu'une route d'inscription. La route racine utilise un routeur pour générer automatiquement des routes pour le `CustomUserViewSet`.

Le `CustomUserViewSet` permet de visualiser ou de modifier des utilisateurs. Le viewset inclut une logique personnalisée pour créer un utilisateur et pour déterminer les autorisations pour différentes actions.

Le `CustomUserSerializer` inclut une logique de validation pour garantir que les utilisateurs ont au moins 15 ans.

### Application Projets

L'application Projets est responsable de la gestion des projets au sein de l'application. Elle inclut les modèles `Project` et `Contributor`.

Le modèle `Project` représente un projet au sein de l'application. Chaque projet a un titre, une description et un type.

Le modèle `Contributor` représente un utilisateur qui contribue à un projet. Chaque contributeur a un rôle, des permissions et un indicateur indiquant s'il peut attribuer des problèmes.

L'application inclut les `ProjectViewSet` et `ContributorViewSet` pour gérer respectivement les opérations CRUD liées aux projets et aux contributeurs.

Les `ProjectSerializer` et `ContributorSerializer` sont utilisés pour la sérialisation et la dé-sérialisation des instances de projet et de contributeur.

L'application inclut également des classes de permissions personnalisées telles que `IsProjectOwnerOrReadOnly` et `IsContributorOrReadOnly` pour gérer les permissions au niveau de l'objet.

Les routes URL pour l'application Projets comprennent des routes pour lister tous les projets, récupérer un projet spécifique, mettre à jour un projet, supprimer un projet, lister tous les contributeurs d'un projet, ajouter un contributeur à un projet, mettre à jour un contributeur et supprimer un contributeur d'un projet.

### Application Problèmes

L'application Problèmes est responsable de la gestion des problèmes au sein de l'application. Elle inclut le modèle `Issue`.

Le modèle `Issue` représente un problème au sein d'un projet. Chaque problème a un titre, une description, une étiquette, une priorité, un projet, un statut, un auteur et un assigné.

L'application inclut le `IssueViewSet` pour gérer les opérations CRUD liées aux problèmes.

Le `IssueSerializer` est utilisé pour la sérialisation et la dé-sérialisation des instances de problème.

L'application inclut également des classes de permissions personnalisées telles que `IsAuthorOrReadOnly` pour gérer les permissions au niveau de l'objet.

Les routes URL pour l'application Problèmes comprennent des routes pour lister tous les problèmes, récupérer un problème spécifique, mettre à jour un problème et supprimer un problème.

### Application Commentaires

L'application Commentaires est responsable de la gestion des commentaires au sein de l'application. Elle inclut le modèle `Comment`.

Le modèle `Comment` représente un commentaire sur un problème. Chaque commentaire a une description, un auteur et un problème.

L'application inclut le `CommentViewSet` pour gérer les opérations CRUD liées aux commentaires.

Le `CommentSerializer` est utilisé pour la sérialisation et la dé-sérialisation des instances de commentaire.

L'application inclut également des classes de permissions personnalisées telles que `IsAuthorOrReadOnly` pour gérer les permissions au niveau de l'objet.

Les routes URL pour l'application Commentaires comprennent des routes pour lister tous les commentaires, récupérer un commentaire spécifique, mettre à jour un commentaire et supprimer un commentaire.