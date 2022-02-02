# Backend Interview Homework

- Write down your answers for the following questions and then paste your answers into the "Backend Assignment" quiz on learningsuite. You can use the internet.

    1. What is CI/CD? What are some good CI/CD practices?
    CI/CD stands for Continuous Integration and Continuous Delivery. It is an agile methodology that allows devs to deploy changes faster and more reliably. 
    CI encourages teams to commit to version control and test code more often and CD helps them to deliver the application smoothly.
    2. What is and what are the benefits of using a binary tree?
    A binary tree is a data structure with nodes that have at most two ( a right and left) nodes "below" in a descending "tree" fashion.
    Benefits include: a great way to store hierarchical data, reflect structural relationships, insertion and deletion are faster than linked lists and arrays, flexible.
    3. What does SOLID mean?
    S: Single responsibility
    O: Open-closed
    L: Liskov Substitution
    I: Interface segregation
    D: Dependency inversion
    4. What is abstraction? Give an example.
    Abstraction is the act of purposfully hiding the details of something to focus on other aspects of the idea/structure. For example a user interface is an abstraction of all the processes happening on the back end that make it work.
    5. What is a singleton? Give an example of when to use this principle.
    A singleton is a class that is instantiated only once and can be accessed throughout the system. An example could be a clas that reads env variables from the disk on startup and then all other code simply reads from that one instantiated class instead of calling it again to read from the disk (a slow process)
