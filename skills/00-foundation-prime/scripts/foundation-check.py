#!/usr/bin/env python3
"""
Foundation Prime - Pattern Recognition Validator

This interactive script helps verify understanding of the three foundational patterns:
1. Emergence
2. Composition
3. Transformation
"""

import sys

def print_header(text):
    """Print a formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")

def print_section(text):
    """Print a section divider"""
    print(f"\n--- {text} ---\n")

def get_response(prompt):
    """Get user response"""
    print(f"{prompt}")
    response = input("> ").strip()
    return response

def validate_emergence():
    """Validate understanding of Emergence pattern"""
    print_header("PATTERN 1: EMERGENCE")

    print("Emergence: Complex behavior arises from simple rules applied repeatedly.\n")
    print("Think of a complex system you interact with regularly.")
    print("(Examples: your workplace, a software tool, a creative process, a relationship)\n")

    system = get_response("What system are you analyzing?")

    print(f"\nGreat! Let's analyze: {system}\n")

    simple_rule = get_response("What SIMPLE rule or action happens repeatedly in this system?")
    complexity = get_response("What COMPLEX behavior emerges from that repetition?")
    intervention = get_response("If you changed the simple rule, how would the complex behavior change?")

    print_section("Your Emergence Analysis")
    print(f"System: {system}")
    print(f"Simple rule: {simple_rule}")
    print(f"Emergent complexity: {complexity}")
    print(f"Intervention point: {intervention}")

    print("\n✓ You've identified emergence! You can see how repetition of simple rules creates complexity.")

    return {
        "system": system,
        "simple_rule": simple_rule,
        "complexity": complexity,
        "intervention": intervention
    }

def validate_composition():
    """Validate understanding of Composition pattern"""
    print_header("PATTERN 2: COMPOSITION")

    print("Composition: Small, well-defined pieces combine to create larger capabilities.\n")
    print("Think of something you've built or a skill you've developed.")
    print("(Examples: a project, a recipe, a workflow, a creative piece)\n")

    creation = get_response("What did you build or develop?")

    print(f"\nExcellent! Let's decompose: {creation}\n")

    pieces = get_response("What are the main PIECES that compose it? (List 2-5)")
    interfaces = get_response("How do these pieces CONNECT or interact?")
    reusable = get_response("Which piece could you use in a different context?")

    print_section("Your Composition Analysis")
    print(f"Creation: {creation}")
    print(f"Component pieces: {pieces}")
    print(f"Interfaces: {interfaces}")
    print(f"Reusable piece: {reusable}")

    print("\n✓ You've identified composition! You can see how well-defined pieces combine into larger systems.")

    return {
        "creation": creation,
        "pieces": pieces,
        "interfaces": interfaces,
        "reusable": reusable
    }

def validate_transformation():
    """Validate understanding of Transformation pattern"""
    print_header("PATTERN 3: TRANSFORMATION")

    print("Transformation: Patterns maintain identity while changing form or context.\n")
    print("Think of a skill or pattern you've learned in one area that helped in another.")
    print("(Examples: debugging code → troubleshooting life, music → writing, sports → business)\n")

    original = get_response("What skill/pattern did you learn first? (Domain A)")

    print(f"\nInteresting! Let's trace the transformation of: {original}\n")

    core_pattern = get_response("What's the ESSENTIAL pattern beneath the surface details?")
    new_domain = get_response("Where else have you applied this same pattern? (Domain B)")
    transfer = get_response("How did understanding from Domain A help in Domain B?")

    print_section("Your Transformation Analysis")
    print(f"Original domain: {original}")
    print(f"Core pattern: {core_pattern}")
    print(f"Transferred to: {new_domain}")
    print(f"How it transferred: {transfer}")

    print("\n✓ You've identified transformation! You can see how patterns persist across contexts.")

    return {
        "original": original,
        "core_pattern": core_pattern,
        "new_domain": new_domain,
        "transfer": transfer
    }

def integration_check(emergence, composition, transformation):
    """Check if user can integrate all three patterns"""
    print_header("INTEGRATION: All Three Patterns Together")

    print("The real power comes from seeing how these patterns work together.\n")
    print("Let's apply all three to a single challenge you're facing:\n")

    challenge = get_response("What's a current challenge or goal you have?")

    print(f"\nLet's apply the Foundation to: {challenge}\n")

    print("EMERGENCE: What simple action, repeated, could create the outcome you want?")
    emergence_app = get_response("")

    print("\nCOMPOSITION: What pieces need to work together? How should they connect?")
    composition_app = get_response("")

    print("\nTRANSFORMATION: What pattern from another domain could help here?")
    transformation_app = get_response("")

    print_section("Your Integrated Analysis")
    print(f"Challenge: {challenge}")
    print(f"Emergence strategy: {emergence_app}")
    print(f"Composition strategy: {composition_app}")
    print(f"Transformation strategy: {transformation_app}")

    print("\n✓ You've integrated all three patterns! This is Foundation mastery.")

    return {
        "challenge": challenge,
        "emergence_strategy": emergence_app,
        "composition_strategy": composition_app,
        "transformation_strategy": transformation_app
    }

def generate_summary(emergence, composition, transformation, integration):
    """Generate a summary of pattern recognition ability"""
    print_header("FOUNDATION PRIME: VALIDATION COMPLETE")

    print("You've demonstrated understanding of all three foundational patterns:\n")

    print("✓ EMERGENCE - You can see how simple rules create complexity")
    print(f"  Example: {emergence['simple_rule']} → {emergence['complexity']}")

    print("\n✓ COMPOSITION - You can see how pieces combine into wholes")
    print(f"  Example: {composition['pieces']} compose into {composition['creation']}")

    print("\n✓ TRANSFORMATION - You can see patterns across domains")
    print(f"  Example: {transformation['core_pattern']} from {transformation['original']} to {transformation['new_domain']}")

    print("\n✓ INTEGRATION - You can apply all three together")
    print(f"  Applied to: {integration['challenge']}")

    print("\n" + "="*60)
    print("  YOU HAVE COMPLETED FOUNDATION PRIME")
    print("="*60)

    print("\nYou are now a Pattern Seer—someone who can look at any system and identify")
    print("its emergent properties, compositional structure, and transformational patterns.")

    print("\n🎯 NEXT STEP: You're ready for Stage 1 - The Pattern Weaver")
    print("\nReturn to your AI Narrator and say: 'I see the Foundation. Show me Stage 1.'\n")

def main():
    """Main validation workflow"""
    print_header("FOUNDATION PRIME - Pattern Recognition Validator")

    print("This interactive check will help you verify your understanding of the")
    print("three foundational patterns: Emergence, Composition, and Transformation.")
    print("\nYou'll apply each pattern to something real from your life.")
    print("This isn't theory—it's about seeing patterns in reality.")

    print("\nReady? Let's begin.")
    input("\nPress Enter to start...")

    # Validate each pattern
    emergence = validate_emergence()
    composition = validate_composition()
    transformation = validate_transformation()

    # Integration check
    integration = integration_check(emergence, composition, transformation)

    # Generate summary
    generate_summary(emergence, composition, transformation, integration)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✋ Validation interrupted. Run again when ready to complete the Foundation check.")
        sys.exit(0)
