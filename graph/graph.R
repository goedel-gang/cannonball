library(ggplot2)

soln_df <- read.table("solutions.tsv")
colnames(soln_df) <- c("s", "C", "n_P", "n_C")

trend_df <- subset(soln_df, log10(C) > -3 + 7 * log10(s) &
                            log10(C) < -2.5 + 7.5 * log10(s) &
                            s > 20)

model <- lm(log(C) ~ log(s), data=trend_df)
intercept <- coef(summary(model))["(Intercept)", "Estimate"]
grad <- coef(summary(model))["log(s)", "Estimate"]
print(paste("C =", exp(intercept), "* s ^ ", grad))

ggplot(soln_df, aes(s, C)) +
    geom_point() +
    ggtitle("Log plot of polygonal cannonball numbers") +
    labs(x="Base sides", y="Number") +
    theme(panel.grid.minor = element_line(colour="gray", size=0.4),
          panel.grid.major = element_line(colour="gray", size=1),
          panel.background = element_blank()) +
    scale_x_log10() +
    scale_y_log10() +
    geom_abline(intercept = -3, slope = 7, linetype="dotted") +
    geom_abline(intercept = -2.5, slope = 7.5, linetype="dotted")

ggplot(soln_df, aes(s, C)) +
    geom_point() +
    ggtitle("Linear plot of subrange") +
    labs(x="Base sides", y="Number") +
    theme(panel.grid.minor = element_line(colour="gray", size=0.4),
          panel.grid.major = element_line(colour="gray", size=1),
          panel.background = element_blank()) +
    xlim(0, 1500)

ggplot(trend_df, aes(s, C)) +
    geom_point() +
    ggtitle("Log plot of the subset") +
    labs(x="Base sides", y="Number") +
    theme(panel.grid.minor = element_line(colour="gray", size=0.4),
          panel.grid.major = element_line(colour="gray", size=1),
          panel.background = element_blank()) +
    scale_x_log10() +
    scale_y_log10() +
    geom_smooth(method = "lm", linetype="dashed")
