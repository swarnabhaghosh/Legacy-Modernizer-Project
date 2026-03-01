public class DatabaseService {

    public boolean checkUser(String username, String password) {
        if (username.equals("admin") && password.equals("admin123")) {
            System.out.println("Login Success");
            return true;
        }
        System.out.println("Login Failed");
        return false;
    }
}