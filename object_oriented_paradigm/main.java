public class Main {
    public static void main(String[] args) {
        Library myLibrary = new Library();

        Book book1 = new Book("1984", "George Orwell");
        Book book2 = new Book("To Kill a Mockingbird", "Harper Lee");

        myLibrary.addBook(book1);
        myLibrary.addBook(book2);

        myLibrary.showBooks();
    }
}
