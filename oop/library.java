import java.util.ArrayList;
import java.util.List;

public class library {
    private List<book> books;

    public library() {
        this.books = new ArrayList<>();
    }

    public void addbook(book book) {
        this.books.add(book);
    }

    public void listbooks() {
        for (book book : books) {
            System.out.println("ID: " + book.getId() + ", Title: " + book.getTitle() + ", Author: " + book.getAuthor());
        }
    }
}
