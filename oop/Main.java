public class Main {
    public static void main(String[] args) {
        library library = new library();

        book book1 = new book("1984", "George Orwell", 1);
        book book2 = new book("To Kill a Mockingbird", "Harper Lee", 2);

        library.addbook(book1);
        library.addbook(book2);

        library.listbooks();
    }
}
