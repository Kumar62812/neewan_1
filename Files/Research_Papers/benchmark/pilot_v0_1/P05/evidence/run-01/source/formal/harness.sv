module harness;
    (* anyseq *) reg clk, rst, req;
    wire ack_a, ack_b;
    response_a a(clk, rst, req, ack_a);
    response_b b(clk, rst, req, ack_b);
    reg valid = 0;
    reg edge_seen = 0;
    reg seen_reset = 0;
    reg sampled_request;
    always @($global_clock) begin
        valid <= 1;
        if (!valid) assume(!clk);
        if (valid) begin
            if (!$past(clk) && clk) begin
                assume(rst == $past(rst));
                assume(req == $past(req));
                if (!$past(rst) && edge_seen) assume(!(sampled_request && $past(req)));
                assert(ack_a == ($past(rst) ? 1'b0 : $past(req)));
                if ($past(rst)) assert(ack_b == 0);
                else if (edge_seen) assert(ack_b == sampled_request);
                sampled_request <= $past(rst) ? 1'b0 : $past(req);
                edge_seen <= 1;
                if ($past(rst)) seen_reset <= 1;
            end else begin
                assert(ack_a == $past(ack_a));
                assert(ack_b == $past(ack_b));
            end
        end
        cover(seen_reset && ack_a && !ack_b);
        cover(seen_reset && !ack_a && ack_b);
`ifdef EQUALITY
        if (seen_reset) assert(ack_a == ack_b);
`endif
    end
endmodule
