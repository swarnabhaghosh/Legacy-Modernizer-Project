public class AuthService {

    public boolean validate(String user, String pass) {
        return user.equals("admin") && pass.equals("1234");
    }
}