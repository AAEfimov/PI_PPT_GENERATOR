"""
test_text2ppt.py
test gpt module
"""

__author__ = "UrFU team"
__copyright__ = "Copyright 2024, Planet Earth"

import _io

import text2ppt
import unittest


class TestAddphoto(unittest.TestCase):
    def test_presentage(self):
        defined_list = [
            {
                "Topic": "cited to take your topic test! Here's my response:\n\n**Topic: Quantum Entanglement**\n\n**",
                "Summary": [
                    "** Quantum entanglement is a phenomenon where two or more particles become connected in such a way that their properties are correlated, regardless of the distance between them. This connection allows for instantaneous communication and can even transcend space-time.",
                    "",
                    "**1. Introduction to Quantum Entanglement:** In 1935, Einstein, Podolsky, and Rosen (EPR) proposed an experiment to test the principles of quantum mechanics, which led to the concept of entanglement. Entanglement is a fundamental aspect of quantum theory that challenges our classical understanding of space and time.",
                    "",
                    '**2. Characteristics of Entangled Particles:** When particles are entangled, their properties become correlated. For example, if two entangled particles have opposite spin directions, measuring the spin of one particle will instantly affect the spin of the other, regardless of the distance between them. This phenomenon is known as "quantum non-locality."',
                    "",
                    "**3. Entanglement and Quantum Teleportation:** Imagine sending a message from one end of the universe to the other without physically moving any particles. This is essentially what quantum teleportation achieves using entangled particles. The information is transmitted through the connection, bypassing space-time constraints.",
                    "",
                    "**4. EPR Paradox:** The EPR paradox arises when attempting to measure the properties of an entangled particle while keeping its partner unchanged. According to the principles of quantum mechanics, measuring one particle will instantly affect the other, even if they are separated by vast distances.",
                    "",
                    "**5. Bell's Theorem:** In 1964, physicist John Bell refined the EPR paradox, introducing a mathematical framework that further solidified the concept of entanglement. Bell's theorem demonstrated that any local hidden variable theory (LHVT) cannot fully account for the correlations observed in entangled systems.",
                    "",
                    '**6. Entanglement Swapping:** When two particles are entangled, they can be connected to form an "entanglement network." This allows for the transfer of entanglement between different particles, enabling quantum communication and information processing across vast distances.',
                    "",
                    "**7. Applications of Quantum Entanglement:** The potential applications of quantum entanglement are numerous, including:",
                    "",
                    "* Secure quantum communication (quantum cryptography)",
                    "* Quantum computing and simulation",
                    "* Quantum metrology (precision measurement)",
                    "",
                    "**8. Challenges in Maintaining Entanglement:** Preserving entanglement is crucial for practical applications. However, interactions with the environment can cause decoherence, which destroys the entangled state.",
                    "",
                    "**9. Experimental Verification:** The phenomenon of quantum entanglement has been experimentally verified numerous times using various systems, including:",
                    "",
                    "* Photons (particles of light)",
                    "* Atoms",
                    "* Molecules",
                    "* Superconducting circuits",
                    "",
                    "**10. Future Directions:** Ongoing research in quantum entanglement aims to develop more robust and scalable technologies for harnessing its power. This includes the development of new materials, improved experimental techniques, and theoretical advancements.",
                    "",
                    "I hope this response meets your expectations!",
                ],
            }
        ]
        retval = text2ppt.presentate(defined_list)
        self.assertEqual(type(retval), _io.BytesIO)
