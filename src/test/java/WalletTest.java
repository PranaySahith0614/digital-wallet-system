import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

public class WalletTest {
    private Wallet wallet;

    @BeforeEach
    void setUp() {
        wallet = new Wallet(BigDecimal.valueOf(100));
    }

    @Test
    void depositIncreasesBalance() {
        wallet.deposit(BigDecimal.valueOf(50));
        Assertions.assertEquals(new BigDecimal("150"), wallet.getBalance());
    }

    @Test
    void withdrawDecreasesBalance() {
        wallet.withdraw(BigDecimal.valueOf(40));
        Assertions.assertEquals(new BigDecimal("60"), wallet.getBalance());
    }

    @Test
    void withdrawWithInsufficientFundsThrows() {
        Assertions.assertThrows(IllegalArgumentException.class, () -> wallet.withdraw(BigDecimal.valueOf(200)));
    }

    @Test
    void depositWithNegativeAmountThrows() {
        Assertions.assertThrows(IllegalArgumentException.class, () -> wallet.deposit(BigDecimal.valueOf(-10)));
    }
}
