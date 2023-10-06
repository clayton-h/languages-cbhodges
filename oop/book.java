public class book {
    private String title;
    private String author;
    private int id;

    // book constructor and setters
    public book(String title, String author, int id) {
        this.title = title;
        this.author = author;
        this.id = id;
    }

    // book getters
    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public int getId() {
        return id;
    }
}
