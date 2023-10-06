
// these are classes that are part of the util library
import java.util.ArrayList;
import java.util.List;

public class library {
    private List<book> books;

    public library() {
        // constructor initializes a dynamic array (included as a java class) to store
        // book instances
        this.books = new ArrayList<>();
    }

    // add a book of book type
    public void addbook(book book) {
        this.books.add(book);
    }

    public void listbooks() {
        for (book book : books) {
            // built-in class to access system resources (System) and output via I/O stream
            // (.out) and print line (println)
            System.out.println("ID: " + book.getId() + ", Title: " + book.getTitle() + ", Author: " + book.getAuthor());
        }
    }

    // ready for garbage collector
    public void destroy() {
        this.books = null;
    }
}
