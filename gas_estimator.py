# Calculate estimated transaction fee under EIP-1559 standards
def estimate_tx_fee(base_fee_gwei, priority_fee_gwei, gas_limit=21000):
    total_fee_gwei = (base_fee_gwei + priority_fee_gwei) * gas_limit
    # Convert Gwei to Ether format
    total_fee_eth = total_fee_gwei / 10**9
    return total_fee_gwei, total_fee_eth

current_base = 25.5  # Gwei
priority = 1.5      # Gwei

gwei_cost, eth_cost = estimate_tx_fee(current_base, priority)
print(f"Total Gas Cost: {gwei_cost:,} Gwei ({eth_cost:.6f} ETH)")
