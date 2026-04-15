import java.math.BigDecimal;
import java.util.Objects;

public class Wallet {
    private BigDecimal balance = BigDecimal.ZERO;

    public Wallet() {
    }

    public Wallet(BigDecimal initialBalance) {
        if (initialBalance == null) {
            throw new IllegalArgumentException("Initial balance must not be null");
        }
        if (initialBalance.compareTo(BigDecimal.ZERO) < 0) {
            throw new IllegalArgumentException("Initial balance must be zero or positive");
        }
        this.balance = initialBalance;
    }

    public BigDecimal getBalance() {
        return balance;
    }

    public void deposit(BigDecimal amount) {
        validateAmount(amount);
        balance = balance.add(amount);
    }

    public void withdraw(BigDecimal amount) {
        validateAmount(amount);
        if (balance.compareTo(amount) < 0) {
            throw new IllegalArgumentException("Insufficient funds");
        }
        balance = balance.subtract(amount);
    }

    private void validateAmount(BigDecimal amount) {
        if (amount == null) {
            throw new IllegalArgumentException("Amount must not be null");
        }
        if (amount.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Amount must be positive");
        }
    }

    public static void main(String[] args) {
        Wallet wallet = new Wallet(new BigDecimal("100.00"));
        System.out.println("Starting wallet balance: " + wallet.getBalance());
        wallet.deposit(new BigDecimal("50.00"));
        System.out.println("After deposit: " + wallet.getBalance());
        wallet.withdraw(new BigDecimal("30.00"));
        System.out.println("After withdrawal: " + wallet.getBalance());
    }
}
