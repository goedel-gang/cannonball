library(ggplot2)

pdf(NULL)

interesting_df <- read.table("interesting.tsv")
colnames(interesting_df) <- c("s", "C", "n_P", "n_C")

boring_df <- read.table("boring.tsv")
colnames(boring_df) <- c("s", "C", "n_P", "n_C")

all_df <- read.table("all.tsv")
colnames(all_df) <- c("s", "C", "n_P", "n_C")

model <- lm(log(C) ~ log(s), data=boring_df)
intercept <- coef(summary(model))["(Intercept)", "Estimate"]
grad <- coef(summary(model))["log(s)", "Estimate"]
boring_df$fit <- exp(intercept) * boring_df$s ^ grad
boring_df$err <- abs((boring_df$fit / boring_df$C) - 1)
cat("\\begin{equation*}\n")
cat("C =", exp(intercept), "\\cdot s ^ {", grad, "}\n")
cat("\\qquad \\text{Average percentage error of ",
    100 * mean(boring_df$err), "\\%}")
cat("\\end{equation*}\n")

ggplot(all_df, aes(s, C)) +
    geom_point(shape=16) +
    ggtitle("Log plot of polygonal cannonball numbers") +
    labs(x="s - sides of base polygon", y="C - number of cannonballs") +
    theme(panel.grid.minor = element_line(colour="gray", size=0.4),
          panel.grid.major = element_line(colour="gray", size=1),
          panel.background = element_blank()) +
    scale_x_log10() +
    scale_y_log10() +
    geom_abline(intercept = -3, slope = 7, linetype="dotted") +
    geom_abline(intercept = -2.5, slope = 7.5, linetype="dotted")
ggsave("all_log.png")

ggplot(boring_df, aes(s, C)) +
    geom_point(shape=16) +
    ggtitle("Linear plot of boring bits") +
    labs(x="s - sides of base polygon", y="C - number of cannonballs") +
    theme(panel.grid.minor = element_line(colour="gray", size=0.4),
          panel.grid.major = element_line(colour="gray", size=1),
          panel.background = element_blank())
ggsave("boring_lin.png")

ggplot(boring_df, aes(s, C)) +
    geom_point(shape=16) +
    ggtitle("Log plot of the subset") +
    labs(x="s - sides of base polygon", y="C - number of cannonballs") +
    theme(panel.grid.minor = element_line(colour="gray", size=0.4), panel.grid.major = element_line(colour="gray", size=1),
          panel.background = element_blank()) +
    scale_x_log10() +
    scale_y_log10() +
    geom_smooth(method = "lm", linetype="dashed", color="red")
ggsave("boring_log.png")

ggplot(interesting_df, aes(s, C)) +
    geom_point(shape=16) +
    ggtitle("Log plot of interesting bits") +
    labs(x="s - sides of base polygon", y="C - number of cannonballs") +
    theme(panel.grid.minor = element_line(colour="gray", size=0.4),
          panel.grid.major = element_line(colour="gray", size=1),
          panel.background = element_blank()) +
    scale_x_log10() +
    scale_y_log10()
ggsave("interesting_log.png")
