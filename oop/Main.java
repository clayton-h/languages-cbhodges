
// Clayton Hodges & ChatGPT
//
// C for Composition
// classes are composed of instances of other classes
//
// Java code for a library of books
//

public class Main {
    public static void main(String[] args) {
        library library = new library();

        book book1 = new book("1984", "George Orwell", 1);
        book book2 = new book("To Kill a Mockingbird", "Harper Lee", 2);
        // my favorite book - I learned that the "title:", "author:", and "id:"
        // are auto-generated, just pass the parameters as usual
        book book3 = new book("Odyssey", "Homer", 3);

        library.addbook(book1);
        library.addbook(book2);
        // add book to library
        library.addbook(book3);

        library.listbooks();

        // ready for garbage collector
        library.destroy();
        book1 = null;
        book2 = null;
        book3 = null;
    }
}
