module p02_properties(input wire clk, rst, d, q);
    reg past_valid = 1'b0;
    reg loaded_one = 1'b0;
    reg reset_after_one = 1'b0;
    always @($global_clock) begin
        past_valid <= 1'b1;
        if (past_valid) begin
            if (!$past(clk) && clk) begin
                if ($past(rst)) assert(q == 1'b0);
                else assert(q == $past(d));
                cover($past(rst) && $past(d) && q == 0);
                cover(!$past(rst) && !$past(d) && q == 0);
                cover(!$past(rst) && $past(d) && q == 1);
                if (!$past(rst) && $past(d)) loaded_one <= 1;
                if (loaded_one && $past(rst)) reset_after_one <= 1;
                cover(reset_after_one && !$past(rst) && $past(d) && q == 1);
            end else begin
                assert(q == $past(q));
                cover(q && rst && !$past(rst) && !clk && !$past(clk));
                cover(q && rst && !$past(rst) && clk && $past(clk));
            end
        end else begin
            cover(q == 0);
            cover(q == 1);
        end
    end
endmodule
