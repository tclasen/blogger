# blogger

An example project of how to produce sane versioned build artifacts in a micro-service setup with multiple interfaces.

## Definition of an Interface

And interface is a contract between system and the environment it runs in.

## Types of Interfaces

There are 4 elements that are part of every system / environment combination:

1. Human
2. Software
3. Hardware
4. Data

And between these 4 elements, there are 7 ways they can interface with each other. The names we give them change depending on the combination:

* User Interface:
    * Human <-> Software
* User Manual:
    * Human <-> Hardware
* Application Programming Interface:
    * Software <-> Software
* Application Binary Interface:
    * Software <-> Hardware
* Format Specification:
    * Software <-> Data
* Hardware Specification:
    * Hardware <-> Hardware
* Serialziation Specification:
    * Hardware <-> Data

## What is a well defined interface

We don't need to version our code implementation, just the code interfaces. But before we before we put in the effort of figuring out versions, we should define where our interfaces are:

In this example, we have an user and 3 components. The interface between the user and our react page is a UI, but more specifically a web-UI. The interface between react and our FastAPI server is an API, or more specifically a REST API. And there is another API between our FastAPI server and the database that we will call the DB-API.

```
Note: <*> is a "public" interface
Human <*> React <-> FastAPI <-> PostGres
      Web-UI    REST API    DB-API
```

In the above usage stack, we need to define the boundary between our application and the user. If the whole application stack is only ours internally, the only interface we need to be concerned with is the web-ui. Any changes between the react and FastAPI won't have any impact on the consumers of our application.

```
Note: <*> is a "public" interface
Human <*> React <*> FastAPI <-> PostGres
      Web-UI    REST API    DB-API
```

If we were to additionally make the REST API publicly consumable along with the client web-ui, then it also has to be independantly versioned and maintained.

If we have more than one public interface, how do you determine the version of the whole application stack for deployment purposes?

```python
def version(stack):
    return max(componet.version for component in stack if component.interface is public)
```

If an interface is a contract, for every type of interface, there is usually a well defined standard that describes how that contract should be built or what it should contain. For a REST API, you can look to OpenAPI3 as a specification. Or for a data interchange format, JSON is usually the standard.
## What is a well behaved interface

[User Experience Honeycomb](https://www.usability.gov/what-and-why/user-experience.html)

- Usable: Is the design of the system easy and simple to use? The application should feel familiar, and it should be easy to use.

- Useful: Does the application fulfill a need? A business’s product or service needs to be useful.

- Desirable: Is the design of the application sleek and to the point? The aesthetics of the system should be attractive, and easy to translate.

- Findable: Are users able to quickly find the information they're looking for? Information needs to be findable and simple to navigate. A user should never have to hunt for your product or information.

- Accessible: Does the application support enlarged text without breaking the framework? An application should be accessible to those with disabilities.

- Credible: Does the application exhibit trustworthy security and company details? An application should be transparent, secure, and honest.

- Valuable: Does the end-user think it's valuable? If all 6 criteria are met, the end-user will find value and trust in the application.

## Semantic Versioning

[Semantic Versioning](https://semver.org/)

{MAJOR}.{MINOR}.{PATCH}-{TAG}

Increment MAJOR: Used for non-backwards compatible changes or breaking changes

Increment MINOR: Add features or functionality without breaking existing functionality

Increment PATCH: Modify logic, fix bugs, or fix security issues

Increment (Or Change) TAG: You need to differentiate versions

Example:

1. Moving from 1.0.0 to 1.1.0 indicates a minor release that may add new features.

2. Moving from 1.1.0 to 2.0.0 incidates a non-backwards compatible change was introduced. The product is the same, but the interfaces are different.

3. Moving from 2.0.0-rc3 to 2.0.0 means that release candidate 3 of the major release 2.0.0 has been promoted to version 2 and the product is finally release. Yay!

4. Using the version: 3.0.2-6b93616 is probably a unique tag generated based off of a version control system hash for the current commit. This is used when you need to build and ship a unique versioned build artifact, but you don't want it to conflict with other existing artifacts. `$(git rev-parse --verify HEAD --short)`

Speaking of which...

## Build Artifacts

Who is the consumer of my product and how will they consume the product? At which interfaces will interact with your product and how will they deploy it?

- Are you rapid prototyping or just doing local development
    - Use a source tar ball

- Are you creating a library other Python developers?
    - Create a Python wheel

- Do you need a user to install your app directly onto their operating system?
    - Package that wheel in a native format such as DEB, RPM, or MSI

- Do you need protect trade secrets?
    - Compile your code first using pyc, cython, or nuitka

- Is your application meant to be shipped as a container?
    - Package an above step into an OCI Image

- Is your application meant to be run in Kubernetes?
    - Publish a bunch of yaml or a helm chart tagged with the above OCI image tag
