public class UserService {

    private DatabaseService databaseService;

    public UserService() {
        databaseService = new DatabaseService();
    }

    public boolean login(String username, String password) {
        if (validate(username, password)) {
            return databaseService.checkUser(username, password);
        }
        return false;
    }

    private boolean validate(String username, String password) {
        return username != null && password != null && password.length() > 5;
    }
}