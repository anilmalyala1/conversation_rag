public class Logger {

    public void print(String message) {
        System.out.println(message);
    }

    public void print(int number) {
        System.out.println(number);
    }

    public static void main(String[] args) {
        Logger logger = new Logger();
        logger.print("Logging message...");
        logger.print(123);
    }
}