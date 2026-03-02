public class UserService {

    AuthService auth = new AuthService();

    public boolean login(String username, String password) {
        return auth.validate(username, password);
    }
}