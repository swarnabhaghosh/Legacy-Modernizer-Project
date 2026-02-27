public class Login {

    public void login() {
        validateUser();
        connectDB();
    }

    private void validateUser() {
        System.out.println("Validating");
    }

    private void connectDB() {
        System.out.println("Connecting");
    }
}